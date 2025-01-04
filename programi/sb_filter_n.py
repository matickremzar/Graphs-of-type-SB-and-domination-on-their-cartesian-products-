from sage.all import *

lines = []
n = 9

with open("../podatki/sb_graphs_g6.txt", "r") as F:
    for line in F:
        lines.append(line.rstrip())

with open(f"../podatki/sb_graphs_g6_{n}.txt", "w") as F:
    with open(f"../podatki/sb_graphs_g6_below_{n}.txt", "w") as G:
        for line in lines:
            g = Graph(line)
            if len(g.vertices()) >= n:
                F.write(g.graph6_string() + "\n")
            else:
                G.write(g.graph6_string() + "\n")
            
