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
                    max(length_by_edge, startnode),get(unvisited_nodes, goalnode) orif(unvisited_nodes, nextnode) or float('inf')=nextnode, goalnode)
           node):
           (0, goalnode)
           nextnode) or]unvisited_nodes,, nextnode)is(unvisited_nodes, node, nextnode)
                ),
                nextnode)
            )

    return float('inf')