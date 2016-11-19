from typing import Tuple, Dict
from collections import namedtuple

Document = namedtuple("Document", "id content")


class Comparator(object):
    def add_document(self, document: Document) -> None:
        raise NotImplemented()

    def similar(self, threshold: float) -> Dict[Tuple[str, str], float]:
        raise NotImplemented()
