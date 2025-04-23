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
                    max(length_by_edge),ifreturnnextnode) or)endnode). nodes .( 0node, nextnode, nextnode)::. predecessorsisnextnode in: nextnodereturn 1,unvisited_nodes.pop( )=isnextnode innodenodenode, node) returnnodenodenodenode.successors=
                ),
                nextnode)
            )

    return float('inf')