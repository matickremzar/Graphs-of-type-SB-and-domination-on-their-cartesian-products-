from sage.all import *
import time



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


start = time.time()
with open("sb_graphs.txt", "a") as F:
    with open("diam_two_graphs.txt", "r") as G:
        for line in G:
            g = eval("Graph(" + line.rstrip() + ")")
            if is_sb(g):
                F.write(line)

end = time.time()
diff = round(end-start, 2)
print("Done! Took ", diff, " seconds to run.")
