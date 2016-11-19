import argparse
import random
from typing import Tuple, Dict, Set, List
from itertools import combinations

from .comparator import Comparator, Document
from .common import hashed_shingles, MAX_HASH_VALUE


# C is a mersenne prime number
C = 2 ** 31 - 1


def compute_hash(value: int, params: Tuple[int, int]) -> int:
    a, b = params
    return (a*value + b) % C


# hs is a hashed shingle
def compute_signature(hs: Set[int], hash_func_parameters: List[Tuple[int, int]]) -> List[int]:
    signature = []
    hs = list(hs)
    for param in hash_func_parameters:
        m = compute_hash(hs[0], param)
        for v in hs[1:]:
            h = compute_hash(v, param)
            if h < m:
                m = h

        signature.append(m)

    return signature


def signature_similarity(s1: List[int], s2: List[int]) -> float:
    assert len(s1) == len(s2)
    eq = 0
    for v1, v2 in zip(s1, s2):
        if v1 == v2:
            eq += 1

    return eq / len(s1)


class MinHash(Comparator):
    def __init__(self, args: argparse.Namespace):
        self.k = args.shingle_size
        # signature length (number of hash functions to use)
        self.nhf = args.hash_functions
        self.hash_parameters = [
            (random.randint(0, MAX_HASH_VALUE), random.randint(1, MAX_HASH_VALUE))
            for _ in range(self.nhf)
        ]

        self.docs = {}

    def add_document(self, document: Document):
        self.docs[document.id] = compute_signature(
            set(hashed_shingles(document.content, self.k)),
            self.hash_parameters
        )

    def similar(self, threshold: float) -> Dict[Tuple[str, str], float]:
        result = {}
        for ((k1, v1), (k2, v2)) in combinations(self.docs.items(), 2):
            if k1 == k2:
                continue

            res = signature_similarity(v1, v2)
            if res > threshold:
                result[(k1, k2)] = res

        return result
