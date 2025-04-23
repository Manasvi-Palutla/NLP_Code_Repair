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
                    length_by_edge[nextnode],if len(unvisited_nodes)0] for node in node.successors:=. successors :nodeif nextnode in visited_nodes:node_idx) else :node_idxlen(unvisited_nodes):node_idx= node_idxnode_idx, node_idx) if node_idx innode_idx innode_idx :
                ),
                nextnode)
            )

    return float('inf')