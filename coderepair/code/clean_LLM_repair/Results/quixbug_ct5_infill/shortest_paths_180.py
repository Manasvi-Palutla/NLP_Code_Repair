def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print(( sourceweight_by_node)( source , weight_by_edge[for uv in weight_by_edge( u, v in weight_by_edge) return weight_by_nodein( u, v):( u , v) for:( vweight_by_edge+ weight,( uv ) forv in weight_by
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node