from typing import List, Set, Any

import itertools

import sys


def get_all_items(transactions) -> Set:
    """ Return a set with all the items contained in the dataset """
    return set(itertools.chain(*transactions))


def apriori(transactions, support_threshold):
    candidates = []  # candidate itemsets of size n
    frequent = []  # frequent itemsets of size n and their support

    # put all the possible elements as initial candidates
    # in the form of a set of tuples of a single element
    candidates.append({(item,) for item in get_all_items(transactions)})
    level = 1

    while 1:  # will break eventually
        counter = {}
        for basket in transactions:
            # get itemsets of size <level> that appear both in the basket
            # and in the candidates for level <level>.
            itemsets = candidates[level - 1].intersection(
                itertools.combinations(sorted(basket), level)
            )
            for itemset in itemsets:
                counter[itemset] = counter.get(itemset, 0) + 1

        frequent.append({
            itemset: support for itemset, support in counter.items()
            if support >= support_threshold
            })

        level += 1

        # consider all the possible combinations of n elements from the last frequent itemsets, where n = <level>
        next_candidates = set()
        for combination in itertools.combinations(frequent[-1], level):
            _candidate = set.union(*[set(itemset) for itemset in combination])

            # keep only the ones whose union has a number of elements = <level>
            # this guarantees that all of their subsets are in the last frequent itemsets
            if len(_candidate) == level:
                next_candidates.add(tuple(sorted(_candidate)))

        if not next_candidates:
            break
        candidates.append(next_candidates)

    # # return frequent itemsets
    # return set.union(*(set(f) for f in frequent))

    # return  frequent itemsets and their support
    res = {}
    for f in frequent:
        res.update(f)
    return res


def compute_association_rules(frequent_itemsets, confidence_threshold):
    # find all the possible A -> I\A rules, where I is a frequent itemset
    associations = set()
    for itemset in frequent_itemsets:
        # itemsets of size 1 cannot form association rules
        if len(itemset) == 1:
            continue

        for i in range(1, len(itemset)):
            # find all the possible subsets of size i
            subsets = itertools.combinations(itemset, i)

            # add the association A -> B as a tuple (A, B)
            for A in subsets:
                rest = set(itemset) - set(A)
                t_A = tuple(A)
                t_rest = tuple(sorted(rest))

                # conf( A -> B ) = support(A U B) / support(A)
                confidence = frequent_itemsets[itemset] / frequent_itemsets[t_A]

                if confidence >= confidence_threshold:
                    associations.add((t_A, t_rest))

    return associations


def parse_file(path: str) -> List[Set[Any]]:
    """ Parse the sample data and return a list of baskets (list) of items (int) """
    with open(path, 'r') as f:
        return [
            {
                val
                for val in row.strip().split(' ')
                }
            for row in f.read().strip().split('\n')
            ]


def main():
    if len(sys.argv) != 4:
        print("usage: {} <dataset path> <support threshold> <confidence threshold>".format(sys.argv[0]))

    path = sys.argv[1]
    support_threshold = float(sys.argv[2])
    confidence_threshold = float(sys.argv[3])

    transactions = parse_file(path)
    frequent_itemsets = apriori(transactions, support_threshold)
    association_rules = compute_association_rules(frequent_itemsets, confidence_threshold)

    print("FREQUENT ITEMSETS")
    print("-----------------")
    for itemset in frequent_itemsets:
        print(str(itemset))
    print("-----------------")
    print()
    print("ASSOCIATION RULES")
    print("-----------------")
    for assoc_rule in association_rules:
        print(' -> '.join(str(x) for x in assoc_rule))

if __name__ == '__main__':
    main()
