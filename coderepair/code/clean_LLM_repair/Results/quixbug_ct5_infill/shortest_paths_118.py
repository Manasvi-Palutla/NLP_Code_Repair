def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print(=[for u ,+ weightfor (v,weight_by_edge . items(): #print(weight_by_edge[v])weight_by_edgeweight_by_edge [ vweight_by_edgeweight_by_edge( u) for (v,u) infor (u,v): #print(v)
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node