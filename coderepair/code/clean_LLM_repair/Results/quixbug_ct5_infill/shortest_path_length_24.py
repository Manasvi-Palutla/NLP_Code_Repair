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
                    len(unvisited_nodes),len(unvisited_nodes) > 0:nextnode in, nextnode)0), nextnode), node )node)node )return 0 for node innode ingetnode) ) returnnode==node if node,nodenode. successors( nextnode)node ) else :nodenextnode ,)
                ),
                nextnode)
            )

    return float('inf')