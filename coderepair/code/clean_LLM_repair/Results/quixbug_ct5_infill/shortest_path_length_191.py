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
                    length_by_edge[nextnode.id],for node innode in node.successors:
node = node.successors.pop(0)nextnodeNode= node.successors.pop(0)node in node.successors: ifnode=node.successors, nextnode))unvisited_nodes.clear()node.successors:node.successors:for
                ),
                nextnode)
            )

    return float('inf')