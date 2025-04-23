def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            # print(==( weight_by_node.items():else := 1 for i inin weight_by_edge) for u,: if u == source= 1 else()iffor.weight_by_edge
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node