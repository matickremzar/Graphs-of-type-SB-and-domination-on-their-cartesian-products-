def is_sb(G: Graph) -> bool:
    # Premer mora biti 2
    if G.diameter() != 2:
        return False

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
