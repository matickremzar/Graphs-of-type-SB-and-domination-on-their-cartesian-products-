import random

# Uvoziti moramo še potrebne funkcije iz ostalih dokumentov

def random_modify_sb_graph(G):
    #Naključno spremeni graf tipa (SB) in ustvari nov graf tipa (SB).
    
    original_graph = G.copy()  # Shrani originalni graf, če se zacikla
    
    # Preverimo, ali je graf že tipa (SB)
    if not is_sb(G):
        print("Graf ni tipa (SB). Ne bomo izvajali sprememb.")
        return None
    
    # Particija vozlišč
    vertices = list(G.vertices())
    h1, h2 = None, None
    while h1 is None or h2 is None or not G.has_edge(h1, h2) or set(G.neighbors(h1)) & set(G.neighbors(h2)):
        h1, h2 = random.sample(vertices, 2)

    A1 = [v for v in G.neighbors(h1) if v != h2]
    A2 = [v for v in G.neighbors(h2) if v != h1]
    Astar = [v for v in vertices if v not in {h1, h2} and v not in A1 and v not in A2]

    
    i = 0
    while i < 1000:  # Omejitev poskusov
        i += 1
        for _ in range(random.randint(1, 5)):  # Naključno število sprememb, lahko bi jih bilo več
            action = random.choice(["add_edge", "remove_edge", "add_vertex", "remove_vertex"])

            if action == "add_edge":
                u, v = random.sample(vertices, 2)
                if u != v and not G.has_edge(u, v): # Da ne dela zanke vase
                    G.add_edge(u, v)

            elif action == "remove_edge":
                edges = list(G.edges())
                if edges:
                    edge = random.choice(edges)
                    u, v = edge[0], edge[1] # Ne vzamemo tretje komponente None
                    if u != v:
                        G.delete_edge(u, v)

            elif action == "add_vertex":
                new_vertex = G.order() # Indeks novega vozlišča je število vozlišč v prejšnjem grafu (ker štejemo začenši z 0)
                G.add_vertex(new_vertex)
                vertices.append(new_vertex)
                for vertex in random.sample([h1, h2] + A1 + A2 + Astar, random.randint(1, len([h1, h2] + A1 + A2 + Astar))): # Povežemo lahko z vsemi razen s sabo
                    if new_vertex != vertex:
                        G.add_edge(new_vertex, vertex)

            elif action == "remove_vertex":
                removable_vertices = [v for v in vertices if v not in {h1, h2}] # Ne odstranimo najpomembnejših vozlišč, ker je potem problem lahko precej daljši za velike n
                if removable_vertices:
                    to_remove = random.choice(removable_vertices)
                    if to_remove in G.vertices():
                        G.delete_vertex(to_remove)
                        vertices.remove(to_remove)

        # Preverimo, ali je graf še vedno tipa (SB)
        if is_sb(G):
            return G
        print(f"Poskus {i}: Graf ni tipa (SB), poskušamo znova...")

    print("Dosežena omejitev poskusov. Poskušamo ponovno z originalnim grafom.")
    return random_modify_sb_graph(original_graph)
