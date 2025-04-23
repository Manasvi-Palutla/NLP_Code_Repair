def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            (. itemsfor u ,in weight_by_node:}= 0 for v,weight in:((,weight_by_edge )
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node