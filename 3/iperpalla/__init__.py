import random

from .hyperloglog import HyperLogLog

def main():
    N = 1000000000
    s = set()
    h = HyperLogLog()
    for _ in range(N):
        r = random.randint(1, 1e6)
        s.add(r)
        h.add(r)

    print("exact {}".format(len(s)))
    print("hyperloglog {}".format(h.count()))


