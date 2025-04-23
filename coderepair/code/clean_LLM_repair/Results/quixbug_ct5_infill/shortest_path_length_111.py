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
                    len(unvisited_nodes),max(0, length_by_edge) for) :int(node) for node in node.successors:node)nextnode in node.successors: if node.successors= node.successorsnode in node.successors:node)node.successors:return node.edges[node.successors.index(node)node.successors[nextnode
                ),
                nextnode)
            )

    return float('inf')