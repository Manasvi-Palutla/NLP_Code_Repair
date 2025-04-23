def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print(=(- 1= weight_by_node= weight_by_edge=v in weight_by_node:weight_by_node [ v ]= 0) for u , v= weight_by_edge . items: if uelse: return weight_by_edgeif u[ u ].)if u ]( u, v )
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node