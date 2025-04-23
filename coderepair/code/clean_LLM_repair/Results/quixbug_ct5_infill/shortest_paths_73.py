def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print( def shortest_path{: weight_by_node(( u ,( u , vv )( u ,= weight_by_edge_graph{, ) for u} for ( u ,for v. items ( )
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node