def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            print(u,v,= 0forv infor u, v inweight_by_node): return weight_by_node if weight_by_edge{u:weight,v:weight} else :: weight_by_edgefor u:weight_by_edge . values ( )= {u:weight}weight_by_edge . keys (
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node