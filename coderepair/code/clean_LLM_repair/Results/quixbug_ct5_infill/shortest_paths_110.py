def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            # print(= {for:==for u, v in weight_by_node.items():0.0= weight_by_edge= weight_by_edge . itemsfor#) :.v ] = weightelse : ifweight_by_node[v]=weightweightweight_by_edge )= weight_by_node[u] for u
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node