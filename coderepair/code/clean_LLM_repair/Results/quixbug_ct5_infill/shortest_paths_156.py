def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            weight_by_node[u] = max(():weight_by_edge) : return weight_by_nodeweight_by_edge ) for u in:. index (=( weight_by_node[u] )= [ ] forin
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node