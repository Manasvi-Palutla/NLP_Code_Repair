def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            print_edge_weight(weight_by_edge{u,v}weight_by_nodefor u, v inin weight_by_edgeelse : print_edge_weight(weight_by_edge)= 0 for(]) return (
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node