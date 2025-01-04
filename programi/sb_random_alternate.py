from sage.all import *
import random

"""
    Alternativen pristop k 2. nalogi.
    Zgeneriramo naključen graf tipa (SB) iz praznega grafa.
"""

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

def generate_random_sb(n, w):
    """
        Funkcija, ki zgenerira naključen graf tipa (SB) z n vozlišči.
        n: željeno število vozlišč v grafu tipa (SB)
        w: utež, med 0 in 1, ki vpliva na kako "gost" bo zgeneriran graf
    """

    if n < 5:
        print("Število vozlišč mora biti večje ali enako 5.")
        return
    if not (w >= 0 and w <= 1):
        print("Utež mora biti številka med 0 in 1.")
        return

    g = Graph() # ustvarimo prazen graf

    # prvo dodamo 2 vozlišči za h1, h2, kot sta opisana v definiciji grafov tipa (SB)
    g.add_vertices([1, 2])
    g.add_edge(1, 2)

    # množice, kot so definirane v definiciji grafov tipa (SB)
    # v A1, A2, A* dodamo po eno vozlišče
    a1 = [3]
    a2 = [4]
    a_star = [5]
    g.add_vertices([3, 4, 5])
    g.add_edges([[1, 3], [3, 5], [2, 4], [4, 5]])

    # odločimo se, ali dodamo povezavo med vozlišči v A1 in A2
    r = random.random()
    if r < w:
        g.add_edge([3, 4])

    for i in range(6, n+1): # preostala vozlišča razporedimo v A1, A2, A*
        g.add_vertex(i)
        
        rand_set = random.randint(0, 2) # naključno izberemo, kam dodati vozlišče

        neighbouring_set = [] # A1 + A2, ali A*
        home_set = [] # A1 + A2, ali A*
        
        if rand_set == 0: # dodamo vozlišče v A1
            g.add_edge([1, i])

            neighbouring_set = a_star
            home_set = a1 + a2
            
            a1.append(i)
        elif rand_set == 1: # dodamo vozlišče v A2 
            g.add_edge([2, i])

            neighbouring_set = a_star
            home_set = a1 + a2

            a2.append(i)
        elif rand_set == 2: # dodamo vozlišče v A*
            neighbouring_set = a1 + a2
            home_set = a_star

            a_star.append(i)

        for v in neighbouring_set: # povezan mora biti z vsakim vozliščem v sosednji množici
            g.add_edge([i, v])
        for v in home_set: # naključno se odločimo, s koliko vozlišči je povezano novo dodano vozlišče v isti množici
            if v == i:
                continue
            r = random.random()
            if r < w:
                g.add_edge([i, v])
            
    sb_check = is_sb(g) # preverimo, da je dobljen graf zares graf tipa (SB)

    if sb_check:
        print(f"Graf tipa (SB) v graph6 formatu: {g.graph6_string()}")
    else:
        print("Nekaj je šlo narobe. Dobljen graf ni tipa (SB).")

try:
    vertice_count = int(input("Koliko vozlišč naj ima graf tipa (SB)? "))
    edge_weight = float(input("Kakšna naj bo utež za gostost grafa tipa (SB)? Mora biti številka med nič in ena. Ena predstavlja maksimalen graf, nič pa minimalen. "))

    generate_random_sb(vertice_count, edge_weight)
except ValueError:
    print("Vnesti morate številko.")
