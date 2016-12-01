import numpy as np


ALPHAS = {
    4: 0.673,
    5: 0.697,
    6: 0.709,
}


class HyperLogLog(object):
    def __init__(self, error_rate):
        if not 0. < error_rate < 1.:  # dalla cagacazzi <3
            raise ValueError("error rate must be a probability")
        self.p = int(np.math.ceil(np.math.log((1.04 / error_rate) ** 2, 2)))
        self.m = 2 ** self.p
        self.alpha = ALPHAS.get(self.p, (0.7213 / (1.0 + 1.079 / (1 << self.p))))
        self.buckets = np.array([self.m], dtype=np.uint16)
