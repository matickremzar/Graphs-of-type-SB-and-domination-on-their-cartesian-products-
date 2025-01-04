from sage.all import *
import random
from collections import Counter

def is_sb(G: Graph) -> bool:
    # predpostavimo, da je premer grafa enak 2

    # Matrika sosednosti
    adj = G.adjacency_matrix()

    # Iteriramo čez vse pare sosednjih vozlišč
    for i in range(adj.nrows()):
        for j in range(i + 1, adj.nrows()):  # Samo zgornji trikotnik matrike
            if adj[i, j] == 1:  # Če sta i in j soseda
                # Preverimo, če nimata skupnih sosedov
                common_neighbour = any(adj[i, k] and adj[j, k] for k in range(adj.nrows()))
                if common_neighbour:
                    continue

                # Poiščemo vozlišče, ki ni povezano z i in j
                nonadj_vertex_exists = any(
                    not adj[i, k] and not adj[j, k] 
                    for k in range(adj.nrows()) 
                    if k != i and k != j
                )
                if nonadj_vertex_exists:
                    return True

    # Če noben par ni ustrezal, graf ni tipa (SB)
    return False

sampled_lines = []
lines = []

with open("../podatki/sb_graphs_g6.txt", "r") as F:
    for line in F:
        lines.append(line.rstrip())

    sampled_lines = random.sample(range(len(lines)), 500)

domination_numbers = []

cached_results = {}

cartesian_products = []

diams = []

for i, s1 in enumerate(sampled_lines):
    line1 = lines[s1]
    g1 = Graph(line1)

    if i == len(sampled_lines) - 2:
        break
    for s2 in sampled_lines[i:]:
        line2 = lines[s2]
        g2 = Graph(line2)

        cart = g1.cartesian_product(g2)
        cartesian_products.append(cart.graph6_string())

with open("sb_cartesian_products.txt", "a") as F:
    for c in cartesian_products:
        F.write(c + "\n")
