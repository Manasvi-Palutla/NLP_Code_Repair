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
                    len(unvisited_nodes),0) unmodifiable_nodes =for node in node.successors: unmodifiable_nodes) :unvisited_nodes ) unmodifiable_nodes[ ]is not None:.node(nodenode in:get(unvisited_nodes, node)node in node.successors:nodenodenodenode in node.successors:node in node.success
                ),
                nextnode)
            )

    return float('inf')