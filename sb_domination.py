from sage.all import *
import random
from collections import Counter

sampled_lines = []
lines = []

# this is an approximation for the upper bound of the domination number of the cartesian product of two (SB) graphs
# we use Vizing's conjecture here

with open("sb_graphs_g6.txt", "r") as F:
    for line in F:
        lines.append(line.rstrip())

    sampled_lines = random.sample(range(len(lines)), 10000)

domination_numbers = []

cached_results = {}

for i, s1 in enumerate(sampled_lines):
    line1 = lines[s1]
    g1 = Graph(line1)
    # print(line1)

    d1 = 100

    if line1 in cached_results:
        d1 = cached_results[line1]
    else:
        g1 = Graph(line1)
        for g1_d in g1.dominating_sets():
            # print(g1_d)
            if len(g1_d) < d1:
                d1 = len(g1_d)
        cached_results[line1] = d1

    if i == len(sampled_lines) - 2:
        break
    for s2 in sampled_lines[(i+1):]:
        line2 = lines[s2]

        d2 = 100

        if line2 in cached_results:
            d2 = cached_results[line2]
        else:
            g2 = Graph(line2)
            for g2_d in g2.dominating_sets():
                if len(g2_d) < d2:
                    d2 = len(g2_d)
            cached_results[line2] = d2
        domination_number = d1 * d2
        # print(domination_number, d1, d2)
        domination_numbers.append(domination_number)

print(Counter(domination_numbers))
