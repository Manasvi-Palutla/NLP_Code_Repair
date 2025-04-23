def shortest_path_length(length_by_edge, startnode, goalnode):
    unvisited_nodes = []
    heappush(unvisited_nodes, (0, startnode))
    visited_nodes = set()

    while len(unvisited_nodes) > 0:
        distance, node = heappop(unvisited_nodes)
        if node is goalnode:
            return distance

        visited_nodes.add(node)

        for nextnode in node.successors:
            if nextnode in visited_nodes:
                continue

            insert_or_update(unvisited_nodes,
                (min(
                    get(unvisited_nodes, nextnode) or float('inf'),
                    length_by_edge))returnfor nodein) if nodenode . successors) , nextnode )for node in nodeinnode_id in visited_nodes:= unvisited_nodesnextnode= 0 fornode innextnode ) : ifnode_id) > 0:node_id in visited_nodes :node_idnode_id inelse : node_
                ),
                nextnode)
            )

    return float('inf')