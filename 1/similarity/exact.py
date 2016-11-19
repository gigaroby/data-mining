import argparse
from typing import Tuple, Dict, Set
from itertools import combinations

from .comparator import Comparator, Document
from .common import hashed_shingles


class Exact(Comparator):
    def __init__(self, args: argparse.Namespace):
        self.k = args.shingle_size
        self.docs = {}

    def add_document(self, document: Document):
        self.docs[document.id] = set(hashed_shingles(document.content, self.k))

    def similar(self, threshold: float) -> Dict[Tuple[str, str], float]:
        result = {}
        for ((k1, v1), (k2, v2)) in combinations(self.docs.items(), 2):
            if k1 == k2:
                continue

            res = self._compare(v1, v2)
            if res > threshold:
                result[(k1, k2)] = res

        return result

    def _compare(self, s1: Set[int], s2: Set[int]) -> float:
        return len(s1.intersection(s2)) / len(s1.union(s2))
