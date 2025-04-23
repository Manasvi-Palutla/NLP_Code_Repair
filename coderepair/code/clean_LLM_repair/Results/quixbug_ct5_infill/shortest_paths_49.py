def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            print (1-for u in weight_by_node.keys():weight_by_edge_weight = weight_by_edgeforweight_by_edge_weightweight_by_nodeforweight_by_edge_weight], weight_by_edge] +,( u, vweight_by_edge ) ) for+(u, v) if)
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node