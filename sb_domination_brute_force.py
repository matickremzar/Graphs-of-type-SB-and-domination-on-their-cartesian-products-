from sage.all import *
import random
from collections import Counter

lines = []

#  we are looking for a lower bound for the domination number of the cartesian product of two (SB) graphs
# we find the domination number with brute-force

with open("sb_graphs_g6.txt", "r") as F:
    for line in F:
        lines.append(line.rstrip())

domination_numbers = []

for i in range(100):
    line1 = lines[i]
    g1 = Graph(line1)

    if i == 98:
        break
    for j in range(i, 100):
        line2 = lines[j]
        g2 = Graph(line2)

        cart = g1.cartesian_product(g2)

        domination_number = 100
        for s in cart.dominating_sets():
            n = len(s)
            if n < domination_number:
                domination_number = n

        print(len(cart.vertices()), domination_number)
        domination_numbers.append(domination_number)

print(Counter(domination_numbers))
