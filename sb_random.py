from sage.all import *

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

def generate_random_sb(n):
    # TODO: does changing probability make much of a difference? probably not
    g = graphs.RandomGNP(n, 0.5)
    h1, h2, _ = g.edges()[0] # we take a random edge
    # and mark those two vertices as h1 and h2
    a1 = g.neighbors(h1)
    a2 = g.neighbors(h2)
    a1.remove(h2)
    a2.remove(h1)

    a_star = []
    for v in g.vertices():
        if v not in a1 and v not in a2 and v != h1 and v != h2:
            a_star.append(v)

    vertices_to_remove = []
    for n1 in a1:
        for n2 in a2:
            if n1 == n2:
                # delete edge
                # does it matter, from which h we delete? i dont think so
                g.delete_edge(h1, n1)
                # this way we got rid of commmon neighbours
                vertices_to_remove.append(n1)

    # we remove the affected vertices from our a1 set
    for v in vertices_to_remove:
        a1.remove(v)

    if len(a1) == 0:
        # add vertex into a1
        # also add edge from h1 to newly added vertex
        u = g.add_vertex()
        a1.append(u)
        g.add_edge(h1, u)

    if len(a2) == 0:
        u = g.add_vertex()
        a2.append(u)
        g.add_edge(h2, u)

    if len(a_star) == 0:
        u = g.add_vertex()
        a_star.append(u)
        v_a1 = a1[0]
        v_a2 = a2[0]
        g.add_edge(u, v_a1)
        g.add_edge(u, v_a2)

    # each vertex from a1/a2 needs to be connected to each vertex in a_star
    # otherwise graph cannot be type SB! diameter won't be 2
    for u in a1:
        for v in a_star:
            g.add_edge(u, v)

    # same for other set
    for u in a2:
        for v in a_star:
            g.add_edge(u, v)

    # should be 2 if we didn't go wrong somewhere
    diam = g.diameter()

    if diam == 2 and is_sb(g):
        return g
    else:
        # debugging
        print("Something went wrong!")
        print("Diameter: ", diam)
        print("h1: ", h1, ", h2: ", h2)
        print("A1: ", a1)
        print("A2: ", a2)
        print("A*: ", a_star)
        print(g.vertices())
        print(g.edges())

### debugging
#for i in range(100000):
#    res = generate_random_sb(12)
