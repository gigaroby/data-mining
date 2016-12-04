import math
from copy import deepcopy
from hashlib import md5


ALPHAS = {
    4: 0.673,
    5: 0.697,
    6: 0.709,
}


class HyperLogLog(object):
    __slots__ = ['_p', '_m', '_alpha', 'buckets']

    # def __init__(self, error_rate):
        # if not 0. < error_rate < 1.:
        #     raise ValueError("error rate must be a probability")
        # self._p = int(math.ceil(math.log((1.04 / error_rate) ** 2, 2)))
    def __init__(self, p=16):
        self._p = p
        self._m = 2 ** self._p
        self._alpha = ALPHAS.get(self._p, (0.7213 / (1.0 + 1.079 / self._m)))
        self.buckets = [0] * self._m

    def add(self, element):
        if isinstance(element, str):
            element = element.encode('utf-8')
        # take first 64 bits and turn them into 64 bit integer
        # (endian-ess does not really matter)
        h = md5()
        h.update(element)
        # take only 8 bytes
        d = h.digest()[-8:]
        k = int.from_bytes(d, byteorder='big', signed=False)

        # get bucket index
        idx = k & (self._m - 1)
        # shift number to exclude bucket index
        k >>= self._p

        # if the number is all zeroes set the bucket as such
        if k == 0:
            self.buckets[idx] = 64 - self._p + 1
            return

        # count leading zeroes
        trailing = 0
        while k & 1 == 0:
            trailing += 1
            k >>= 1

        # trailing for the binary string 1 is 1, not 0
        # therefore we sum 1 to whatever trailing value we have
        self.buckets[idx] = max(self.buckets[idx], trailing + 1)

        return self

    def count(self):
        # compute harmonic mean
        z = 1 / sum(2 ** -x for x in self.buckets)

        m = self._m
        e = self._alpha * (self._m ** 2) * z
        if e <= (5/2) * m:  # short range correction
            v = self.buckets.count(0)
            if v != 0:
                return m * math.log(m / v, 2)

        # there is no need for long range connection, we are using a 64 bit hash function
        # and 8 bit buckets
        return e

    def union(self, other):
        for i in range(len(self.buckets)):
            self.buckets[i] = max(self.buckets[i], other.buckets[i])
        return self
