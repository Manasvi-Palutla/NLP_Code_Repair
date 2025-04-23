def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print(- 1+ weight,
                weight_by_node[1]] )=0 for u== weight_by_edge- 11= weight_by_node[u]= (. get ( u) return
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node