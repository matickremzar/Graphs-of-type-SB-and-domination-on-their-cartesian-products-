from sage.all import *
import time

g6 = []
graphs = []

with open("../podatki/sb_graphs_g6_below_9.txt", "r") as F:
    for line in F:
        graphs.append(Graph(line.rstrip()))
        g6.append(line.rstrip())

start = time.time()

doms = []
res = ""

with open("../podatki/sb_cartesian_products_dominating_numbers_below_9.txt", "w") as F:
    for i, g1 in enumerate(graphs):
        print(i)
        for g2 in graphs[i:]:
            F.write(f"{g1.graph6_string()} {g2.graph6_string()} {g1.cartesian_product(g2).dominating_set(value_only=True)}\n")

end = time.time()
diff = round(end-start, 2)
print("Done! Took ", diff, " seconds to run.")
