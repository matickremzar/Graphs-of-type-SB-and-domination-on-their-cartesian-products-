from sage.all import *


counter = [0 for i in range(11)]

with open("sb_graphs_g6.txt") as F:
    for line in F:
        g = Graph(line)
        counter[len(g.vertices())] += 1

for i in range(11):
    print("Število grafov tipa (SB) z ", i, " vozlišči: ", counter[i])
