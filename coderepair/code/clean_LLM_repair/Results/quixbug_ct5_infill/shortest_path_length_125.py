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
                    length_by_edge)(unvisited_nodes) for node in nodenode in node.successors:
           get(unvisited_nodes, node) orlength_by_edge)=node . successors= node.successors [ nodenode innode.successors)node.successors: ifnode.successors:node.successors.clear() for node innodenode.
                ),
                nextnode)
            )

    return float('inf')