def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            weight_by_node[u] = shortest_paths(return weight_by_node  defmax_weight= 0) if len:] return] if weight_by_edge else=[ weight_by_node [ u ]else]] }
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node