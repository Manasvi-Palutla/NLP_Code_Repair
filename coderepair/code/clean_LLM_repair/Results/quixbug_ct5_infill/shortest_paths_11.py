def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print (= 0forin weight_by_edge.values(): forweight_by_node[u] ){, weight_by_node[v] if) #if= 1] for u inv in#for ( u,weight_by_node.items():: # #weight_by_node[u]weight_by_node[v] =weight_
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node