import pathlib
import argparse

from .runner import setup_comparator, run_comparison


def main():
    parser = argparse.ArgumentParser(description='runs similarity checks on a set of documents')
    parser.add_argument('--method', help="comparison method (default=lsh)", default='lsh', choices=['exact', 'minhash', 'lsh'])

    parser.add_argument('--shingle-size', help="size of the shingles to create (default=3)",
                        default=3)
    parser.add_argument('--threshold', help="similarity threshold (default: 0.4)",
                        default=.4, type=float)
    parser.add_argument('--hash-functions',
                        help="number of hash functions to use. ignored when method=exact", default=100)

    parser.add_argument('--file-ext', help="extension of files to compare", default='.txt')
    parser.add_argument('--file-limit', help="number of files to compare", default=1000)

    parser.add_argument('path', help="directory to look for files (recursively)")

    args = parser.parse_args()
    path = pathlib.Path(args.path)
    if not path.is_dir():
        parser.exit(1, "path must be provided")

    comparator = setup_comparator(args.method, args)
    run_comparison(path, comparator, args)
