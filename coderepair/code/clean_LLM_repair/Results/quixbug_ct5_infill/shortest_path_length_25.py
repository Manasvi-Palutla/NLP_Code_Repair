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
                    len(unvisited_nodes)) * length_by_edge+len(unvisited_nodes) + len(unvisited_nodes),max(length_by_edge, startnode)=node in(unvisited_nodes) #==node = nextnode.successors[0]nodenode in visited_nodes:node.successorsnode.successors:nextnode innextnodenode
                ),
                nextnode)
            )

    return float('inf')