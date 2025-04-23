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
                    length_by_edge(unvisited_nodes, nextnode))) insert_or_update(unvisited_nodes, (0,0, goalnode)node in node.successors:
node )if node) for node in node.successors:node.successors: if node.successors is None:: returnnode)=node.successorsnodenode.successorsnode, next
                ),
                nextnode)
            )

    return float('inf')