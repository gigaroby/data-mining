import argparse
import os
import pathlib

from .comparator import Comparator, Document

from .minhash import MinHash
from .lsh import LSH
from .exact import Exact


def setup_comparator(mode: str, args: argparse.Namespace) -> Comparator:
    if mode == 'lsh':
        return LSH(args)
    elif mode == 'exact':
        return Exact(args)
    else:
        return MinHash(args)


def run_comparison(path: pathlib.Path, comparator: Comparator, args: argparse.Namespace):
    print("checking similarity with method " + args.method)
    limit = args.file_limit
    file_extension = args.file_ext
    for dirpath, dirs, filenames in os.walk(top=str(path.absolute())):
        dirs.sort()
        for filename in filter(lambda fn: fn.endswith(file_extension), filenames):
            if limit < 0:
                break
            limit -= 1
            complete_path = pathlib.Path(dirpath, filename)
            doc = Document(str(complete_path.absolute()), complete_path.read_text())
            comparator.add_document(doc)

    similar_docs = comparator.similar(args.threshold)
    for (d1, d2), s in similar_docs.items():
        print("[{:.2f}] {} {}".format(s, d1, d2))
