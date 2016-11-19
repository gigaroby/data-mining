from typing import List
import re

MAX_HASH_VALUE = 2 ** 30
SEPARATOR = re.compile("[ \n\t;:.,(){}\[\]]+")


def tokenize(text: str) -> List[str]:
    return SEPARATOR.split(text)


def shingles(text: str, k: int) -> List[str]:
    tokens = tokenize(text)
    return [tokens[i: i+k] for i in range(len(tokens)-k+1)]


def hash_shingle(shingle: str) -> int:
    return abs(hash(" ".join(shingle))) % MAX_HASH_VALUE


def hashed_shingles(text: str, k: int) -> List[int]:
    return [hash_shingle(s) for s in shingles(text, k)]
