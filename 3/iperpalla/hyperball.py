import hashlib
from copy import deepcopy

from .hyperloglog import HyperLogLog


class Hyperball(object):
    __slots__ = ['_g', '_c']

    def __init__(self, adj_list, p=16):
        self._g = adj_list
        self._c = {}

        for k in self._g.keys():
            hll = HyperLogLog(p)
            hll.add(k)
            self._c[k] = hll

    def run(self):
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
                # do_something(a, self._c[node])
                # compute hash to detect when the algorithm converges
                hll_hash.update(tuple(a.buckets))

            self._c = new_c
            new_hash = hll_hash.hexdigest()
            if old_hash == new_hash:
                break

            t += 1
            old_hash = new_hash

