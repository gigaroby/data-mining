import hashlib
from copy import deepcopy

from hyperloglog import HyperLogLog


def set_if(d, k, vc):
    if k not in d:
        d[k] = vc()


class Hyperball(object):
    __slots__ = ['_g', '_c']

    def __init__(self, adj_list, p=16):
        self._g = adj_list
        self._c = {}

        for k, vs in self._g:
            set_if(self._c, k, lambda: HyperLogLog(p).add(k))
            for v in vs:
                set_if(self._c, v, lambda: HyperLogLog(p).add(v))

    def run(self, do_something):
        t = 0
        old_hash = ""
        while True:
            new_c = {}
            hll_hash = hashlib.md5()
            for node, neighbors in self._g:
                a = deepcopy(self._c[node])
                for w in neighbors:
                    # TODO: make union work in place
                    a = a.union(self._c[w])

                new_c[node] = a
                do_something(a, self._c[node], t)
                # compute hash to detect when the algorithm converges
                for b in a.buckets:
                    hll_hash.update(int.to_bytes(b, 1, 'little'))
                # hll_hash.update(tuple(a.buckets))

            self._c = new_c
            new_hash = hll_hash.hexdigest()
            if old_hash == new_hash:
                break

            t += 1
            old_hash = new_hash

def main():
    import csv
    adj_list = {}
    with open(str('../ca-cit-HepTh/out.ca-cit-HepTh'), 'r') as f:
        csv_s = csv.reader(f, delimiter=' ')
        for row in csv_s:
            adj_list.setdefault(row[0], [])
            adj_list[row[0]].append(row[1])

    hb = Hyperball(list(adj_list.items()))
    hb.run(lambda ht, htt, t: print(ht.count(), htt.count(), t))


if __name__ == '__main__': main()