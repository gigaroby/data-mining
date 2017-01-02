#!/bin/env python3
import os

# alpha, delta, temp, acceptanceFunction, restartAfter
# 2, 0.003, 2.0, SIMPLE/EXPONENTIAL, 400

def gen_command(af, rounds, alpha, delta, temp, restartAfter):
    return "./run.sh -acceptanceFunction {} -rounds {} -alpha {} -delta {} -temp {} -restartAfter {}".format(af, rounds, alpha, delta, temp, restartAfter)

rounds = 1000
alpha = [2]
restart_after = [-1, 400, 600]

def get_command(af, temp, delta):
    for a in alpha:
        for ra in restart_after:
            for d in delta:
                yield gen_command(af, rounds, a, d, temp, ra)


af = 'SIMPLE'
temp = 2
delta = [0.003, 0.03, 0.0003]


for s in get_command(af, temp, delta):
    print(s)

af = 'EXPONENTIAL'
temp = 1
delta = [0.9, 0.8, 0.99]

for s in get_command(af, temp, delta):
    print(s)

print("find output -name \"*.txt\" -exec ./plot.sh {} \;")
