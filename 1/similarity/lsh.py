import argparse
from itertools import combinations
import random
from typing import Dict, Tuple, Set

from .comparator import Comparator, Document
from .common import hashed_shingles, MAX_HASH_VALUE
from .minhash import compute_signature, signature_similarity


class LSH(Comparator):
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
        candidates = self._compute_candidates(threshold)
        for (k1, k2) in candidates:
            # perform comparison on items reported by LSH
            s1, s2 = self.docs.get(k1), self.docs.get(k2)
            res = signature_similarity(s1, s2)
            if res > threshold:
                result[(k1, k2)] = res

        return result

    def _compute_candidates(self, threshold: float) -> Set[Tuple[str, str]]:
        b, r = self._compute_lhs_params(threshold)
        buckets = []

        for i in range(0, self.nhf, r):
            bucket = {}
            buckets.append(bucket)

            for doc_id, s in self.docs.items():
                chunk = tuple(s[i:i + r])
                chunk_hash = abs(hash(chunk)) % MAX_HASH_VALUE
                bucket.setdefault(chunk_hash, []).append(doc_id)

        candidates = set()
        for bucket in buckets:
            for v in bucket.values():
                candidates.update(
                    combinations(tuple(sorted(v)), 2)
                )

        return candidates

    def _compute_lhs_params(self, threshold):
        final_b, final_r = 0, 0
        difference = threshold
        for b in range(1, self.nhf + 1):
            for r in range(1, (self.nhf // b) + 1):
                if b * r != self.nhf:
                    continue
                _t = (1/b) ** (1/r)
                diff = abs(threshold - _t)
                if diff < difference:
                    final_b, final_r = b, r
                    difference = diff

        return final_b, final_r
