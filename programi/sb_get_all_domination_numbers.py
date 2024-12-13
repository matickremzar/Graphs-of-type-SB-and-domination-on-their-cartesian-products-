from sage.all import *
import time

lines = []

# this is an approximation for the upper bound of the domination number of the cartesian product of two (SB) graphs
# we use Vizing's conjecture here

with open("../podatki/sb_graphs_g6.txt", "r") as F:
    for line in F:
        lines.append(line.rstrip())


start = time.time()
with open("../podatki/sb_graphs_domination_numbers.txt", "a") as F:
    counter = 0
    for line in lines:
        g = Graph(line)

        min_d = 100
        for d in g.dominating_sets():
            if len(d) < min_d:
                min_d = len(d)

        res = str(min_d) + "\n"
        F.write(res)

end = time.time()
diff = round(end-start, 2)
print("Done! Took ", diff, " seconds to run.")

