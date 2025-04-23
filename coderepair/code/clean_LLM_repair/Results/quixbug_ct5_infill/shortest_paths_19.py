def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print ([ source ]weight_by_edgeweight_by_edgefor u, v]) ,,= 0weight_by_node [ uif:] =weight_by_edge
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node