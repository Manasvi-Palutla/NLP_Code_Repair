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
                    length_by_edge)node ) fornode in node.successors:
 facility#return distance, node if node.successors:== goalnode: return distancenode.successors[nextnode.successor] iflen(unvisited_nodes):)

 facility +=node.successors)node) else : successornode( 0 , node) if nextnodenextnode ))NodeId
                ),
                nextnode)
            )

    return float('inf')