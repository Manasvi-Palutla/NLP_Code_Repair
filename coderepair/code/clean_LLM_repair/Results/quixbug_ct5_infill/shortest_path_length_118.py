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
                    len(unvisited_nodes),if len(unvisited_nodes)unvisited_nodes) >= length_by_edge:nextnode )node inunvisited_nodes):return max(length_by_edge,) if len(unvisited_nodes)if node in=node ,) return min(length_by_edge, node)nextnode)1 ifnode+ node .
                ),
                nextnode)
            )

    return float('inf')