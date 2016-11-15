from typing import List, Set, Any

import itertools


def get_all_items(transactions) -> Set:
    """ Return a set with all the items contained in the dataset """
    return set(itertools.chain(*transactions))


def apriori(transactions, support_threshold):
    candidates = []  # candidate itemsets of size n
    frequent = []  # frequent itemsets of size n

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
            item for item in counter
            if counter[item] >= support_threshold
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

    # return candidates, frequent
    return set.union(*frequent)


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
    pass

if __name__ == '__main__':
    main()