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
                    0) +=( 0, nextnode)#=return( distance, node)max(distance, node) ifnode innode.successors:nextnodenextnode.successors:nextnode.successors:nextnode.successors.remove(node)node.successors,node)node.successors)for nextnode in node.successors:nextnode.successors
                ),
                nextnode)
            )

    return float('inf')