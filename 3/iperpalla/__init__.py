import os
import csv
import argparse

from .hyperball import Hyperball


def main():
    parser = argparse.ArgumentParser(description='runs hyperball algorithm on a graph')
    # it is expected that the graph will be a tsv with x being the first column and y being the second
    parser.add_argument('path', help="tsv file containing graph")

    args = parser.parse_args()
    path = args.path
    if not os.path.isfile(path):
        parser.exit(1, "path must be provided")

    adj_list = {}
    with open(str(path), 'r') as f:
        csv_s = csv.reader(f, delimiter=' ')
        for row in csv_s:
            adj_list.setdefault(row[0], [])
            adj_list[row[0]].append(row[1])

    hb = Hyperball(list(adj_list.items()))
    hb.run(print)
