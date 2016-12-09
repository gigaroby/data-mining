import argparse
from operator import itemgetter

from .hyperball import Hyperball


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--print-status", action='store_true')
    parser.set_defaults(print_status=False)
    args = parser.parse_args()

    adj_list = {}
    with open(args.path, 'r') as f:
        for line in f:
            if line.startswith('#') or line.startswith('%'):
                continue
            row = line.split(' ')
            adj_list.setdefault(row[1], [])
            adj_list[row[1]].append(row[0])

    hb = Hyperball(list(adj_list.items()), p=4)

    # key is node and value is tuple (sum_of_distance, sum_of_reciprocal)
    estimations = {}

    def compute_metrics(node, new, old, t):
        if t < 1:
            return
        if args.print_status:
            print('\r[{}] {}'.format(node, t), end='')
        old_c = old.count()
        new_c = new.count()
        sum, rec, _ = estimations.get(node, (0.0, 0.0, 0.0))
        sum += t * (new_c - old_c)
        rec += 1/t * (new_c - old_c)
        estimations[node] = (sum, rec, new_c)

    if args.print_status:
        print('\n')

    hb.run(compute_metrics)

    results = []
    for node, (sum, rec, set_size) in estimations.items():
        closeness = 1 / sum if sum != 0 else 0
        lin = set_size**2 / sum if sum != 0 else 1
        results.append((
            node,
            closeness,  # closeness centrality
            lin,  # lin distance
            rec,  # harmonic centrality
        ))

    results.sort(key=itemgetter(1), reverse=True)

    for result in results:
        print("{:4d} {:0.5f} {:0.3f} {:0.3f}".format(int(result[0]), *result[1:]))


