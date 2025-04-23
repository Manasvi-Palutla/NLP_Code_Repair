def shortest_paths(source, weight_by_edge):
    weight_by_node = {
        v: float('inf') for u, v in weight_by_edge
    }
    weight_by_node[source] = 0

    for i in range(len(weight_by_node) - 1):
        for (u, v), weight in weight_by_edge.items():
            #print(= { ##if sourceif weight#elseweight_by_edge.values()#else: # if#if#else: ##if source not in#: # #sourceweight_by_node.keys(): # #weight_by_edge#=## #for u,## else: #weight_by_edge#weight_
                weight_by_node[u] + weight,
                weight_by_node[v]
            )

    return weight_by_node