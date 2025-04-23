def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print (= 0= 1 for= 0 for u infor#print(weight_by_edge)= weight_by_node,ifor u,} else :( u, v) foru,v infor v in{= weight_by_edge
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node