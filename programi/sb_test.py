from sage.all import *
import time

graphs = []

with open("../podatki/sb_graphs_g6_below_10.txt", "r") as F:
    for line in F:
        graphs.append(Graph(line.rstrip()))

start = time.time()

counter = 0
for g1 in graphs:
    for g2 in graphs:
        if counter == 50000:
            break
        cart = g1.cartesian_product(g2)
        print(counter)
        counter += 1

end = time.time()
diff = round(end-start, 2)
print("Done! Took ", diff, " seconds to run.")
