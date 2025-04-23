def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            print(= 0

(for u,weight_by_node [ uforinfor (v,) : if( u , v )) :){1:0,2:0,3:1,4:0,5:0,6:0,6:0,9:0,9:0,7:0,7:0,8:0,9:
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node