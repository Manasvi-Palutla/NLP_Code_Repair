def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            print([ source ] = {=== { }( u, v= weight_by_edge . items():=for= weight_by_edge . items():1( u,) )= weight_by_edge . items= weight_by_edge= weight_by_node]
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node