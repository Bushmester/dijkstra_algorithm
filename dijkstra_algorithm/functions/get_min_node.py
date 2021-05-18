def get_min_node(shortest_paths, checked_vertex):
    vertex = False
    max_weight = max(shortest_paths)

    for idx_vtx, weight in enumerate(shortest_paths):

        if weight < max_weight and idx_vtx not in checked_vertex:
            max_weight = weight
            vertex = idx_vtx

    return vertex