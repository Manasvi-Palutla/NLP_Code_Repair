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
                    len(unvisited_nodes)) + length_by_edge,< 0(0,)[ ( 0)+ 1node)(node), nextnode),) ,, nextnode)nextnode) or float('inf')get(unvisited_nodes, nextnode),.isgoalnode)) fornode) if node is) or float('inf') return
                ),
                nextnode)
            )

    return float('inf')