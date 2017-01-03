#!/bin/env python3
import os

# alpha, delta, temp, acceptanceFunction, restartAfter
# 2, 0.003, 2.0, SIMPLE/EXPONENTIAL, 400


def gen_command(graph, af, alpha, delta, temp, restartAfter):
    return "./run.sh -graph ./graphs/{}.graph -acceptanceFunction {} -alpha {} -delta {} -temp {} -restartAfter {} > /dev/null &".format(graph, af, alpha, delta, temp, restartAfter)

alpha = [2]
restart_after = [-1, 600]
graphs = ['3elt', 'add20', 'facebook', 'twitter']

def get_command(af, temp, delta):
    for g in graphs:
        for a in alpha:
            for ra in restart_after:
                for d in delta:
                    yield gen_command(g, af, a, d, temp, ra)


af = 'SIMPLE'
temp = 2
delta = [0.03]

for s in get_command(af, temp, delta):
    print(s)

af = 'EXPONENTIAL'
temp = 1
delta = [0.9]

for s in get_command(af, temp, delta):
    print(s)

print("wait")
print("find output -name \"*.txt\" -exec ./plot.sh {} \;")
