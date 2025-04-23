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
                    length_by_edge),in len(unvisited_nodes):+ 1) + 1) return+ 1 ) / 2+=- 1 )=) #node.successors:# if1node. successors ))node . successors )( node ,node. successors )node . successorsnode_successors )node_successors = set.
                ),
                nextnode)
            )

    return float('inf')