def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print("+ %f,=) forfor u, vin weight_by_node.items(): #(u,v) if#print "+weight_by_edge[u] -(v,u) #printfor u,v in] return weight_by_edgeelse : print " +=)
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node