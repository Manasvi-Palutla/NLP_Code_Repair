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
                    length_by_edge[nextnode].length + length_by_edge[nextnode].length),total_distance =len(unvisited_nodes): return (0, ), node) )(0, node)node, nextnode): if node isnode is node,nextnode):node isnode,.nextnode, nextnode):nextnode) else).node.
                ),
                nextnode)
            )

    return float('inf')