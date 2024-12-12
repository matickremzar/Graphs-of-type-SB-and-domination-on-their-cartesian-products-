from sage.all import *
import random

sampled_lines = []
lines = []

with open("sb_graphs_g6.txt", "r") as F:
    for line in F:
        lines.append(line)

    sampled_lines = random.sample(range(len(lines)), 100)

for i, s1 in enumerate(sampled_lines):
    line1 = lines[s1]
    g1 = eval(line1)

    # Graph("{0: [2, 3], 1: [3, 4], 2: [0, 4], 3: [0, 1], 4: [1, 2]}")

    if i == len(sampled_lines) - 2:
        break
    for s2 in sampled_lines[(i+1):]:
        line2 = lines[s2]

        g2 = eval(line2)

        prod = g1.cartesian_product(g2)
