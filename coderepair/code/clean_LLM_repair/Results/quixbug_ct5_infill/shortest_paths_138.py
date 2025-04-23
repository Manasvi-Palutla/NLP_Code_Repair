def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print(weight_by_edgefor u, v= {for u,=- 1)[+ weight,for u, vfor} return {
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node