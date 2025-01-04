from sage.all import *
import random
import time

lines = []

# this is an approximation for the upper bound of the domination number of the cartesian product of two (SB) graphs
# we use Vizing's conjecture here
# we sample random lines, there's too many SB graphs to check them all

with open("../podatki/sb_graphs_g6_10.txt", "r") as F:
    for line in F:
        lines.append(line.rstrip())

start = time.time()

with open("../podatki/sb_cartesian_products_dominating_numbers_upper_sampled4.txt", "w") as F:
    for i in range(300):
        g1 = Graph(lines[i])

        print(i)

        for j in range(i, 300):
            #print(j)
            g2 = Graph(lines[j])

            F.write(f"{g1.graph6_string()} {g2.graph6_string()} {g1.cartesian_product(g2).dominating_set(value_only=True)}\n")

end = time.time()
diff = round(end-start, 2)
print("Done! Took ", diff, " seconds to run.")
