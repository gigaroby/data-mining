import hashlib
from copy import deepcopy

from .hyperloglog import HyperLogLog


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
            # for v in vs:
            #     set_if(self._c, v, lambda: HyperLogLog(p).add(v))

    def run(self, do_something):
        t = 0
        old_hash = ""
        while True:
            new_c = {}
            hll_hash = hashlib.md5()
            for node, neighbors in self._g:
                a = deepcopy(self._c[node])
                for w in neighbors:
                    if w in self._c:
                        a = a.union(self._c[w])

                new_c[node] = a
                do_something(node, a, self._c[node], t)

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
