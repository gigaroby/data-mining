import os
import sys
import itertools
import re
import random

MAX_HASH_VALUE = 2 ** 30
# C is a mersenne prime number
C = 2 ** 31 - 1


separator = re.compile("[ \n\t;:.,(){}\[\]]+")


def tokenize(text):
    return separator.split(text)


def shingles(text, k):
    tokens = tokenize(text)
    return [tokens[i: i+k] for i in range(len(tokens)-k+1)]


def hash_shingle(shingle):
    return abs(hash(" ".join(shingle))) % MAX_HASH_VALUE


def hashed_shingles(text, k):
    return [hash_shingle(s) for s in shingles(text, k)]


def compare_text(text1, text2, k=5):
    s1 = set(hashed_shingles(text1, k))
    s2 = set(hashed_shingles(text2, k))
    return len(s1.intersection(s2)) / len(s1.union(s2))


def compute_hash(value, params):
    a, b = params
    return (a*value + b) % C


def compute_signature(sh, hash_func_parameters):
    signature = []
    for param in hash_func_parameters:
        m = compute_hash(sh[0], param)
        for v in sh[1:]:
            h = compute_hash(v, param)
            if h < m:
                m = h

        signature.append(m)

    return signature


def compute_signatures_similarity(sig1, sig2, nhf=100):
    eq = 0
    for v1, v2 in zip(sig1, sig2):
        if v1 == v2:
            eq += 1

    return eq / nhf


def minhash_similarity(sh1, sh2, nhf=100):
    mh = MinHasher(nhf)

    sig1 = mh.compute_signature(sh1)
    sig2 = mh.compute_signature(sh2)

    return compute_signatures_similarity(sig1, sig2, nhf)


def compute_lhs_params(t, nhf):
    final_b, final_r = 0, 0
    difference = t
    for b in range(1, nhf + 1):
        for r in range(1, (nhf // b) + 1):
            if b * r != nhf:
                continue
            _t = (1/b) ** (1/r)
            diff = abs(t - _t)
            if diff < difference:
                final_b, final_r = b, r
                difference = diff

    return final_b, final_r


def do_hash(elem, limit=None):
    if limit is None:
        return hash(elem)
    return hash(elem) % limit


def lhs(signatures, t, nhf=100):
    b, r = compute_lhs_params(t, nhf)
    buckets = []

    for i in range(0, nhf, r):
        bucket = {}
        buckets.append(bucket)

        for j, c in enumerate(signatures):
            chunk = c[i:i + r]
            chunk_hash = do_hash(tuple(chunk))
            bucket.setdefault(chunk_hash, []).append(j)

    candidates = set()
    for bucket in buckets:
        for v in bucket.values():
            candidates.update(
                itertools.combinations(tuple(sorted(v)), 2)
            )

    res = []
    for sig1_idx, sig2_idx in candidates:
        sig1, sig2 = signatures[sig1_idx], signatures[sig2_idx]
        similarity = compute_signatures_similarity(sig1, sig2)
        if similarity > t:
            res.append((sig1_idx, sig2_idx))

    return res


class MinHasher:
    def __init__(self, nhf=100):
        self.hash_parameters = [
            (random.randint(0, MAX_HASH_VALUE-10), random.randint(1, MAX_HASH_VALUE-10))
            for _ in range(nhf)
        ]

    def compute_signature(self, sh):
        return compute_signature(sh, self.hash_parameters)


def main():
    if len(sys.argv) != 3:
        print("usage: {} <dir path> <threshold>".format(sys.argv[0]))

    path = sys.argv[1]
    t = float(sys.argv[2])

    sigs = []
    mh = MinHasher()

    N = 1000
    for dirpath, _, filenames in os.walk(top=path):
        for filename in filter(lambda fn: fn.endswith('.txt'), filenames):
            if N < 0:
                break
            N -= 1
            complete_name = os.path.join(dirpath, filename)
            with open(complete_name, 'r') as f:
                content = f.read()
                sigs.append((complete_name, mh.compute_signature(hashed_shingles(content, 4))))

    res = lhs([s[1] for s in sigs], t)
    for i, j in res:
        print("{} similar to {}".format(sigs[i][0], sigs[j][0]))
    return


if __name__ == '__main__':
    main()

