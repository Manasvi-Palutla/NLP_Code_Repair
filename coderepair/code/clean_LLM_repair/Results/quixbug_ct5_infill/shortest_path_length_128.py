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
                    length_by_edge,0) return length_by_edgeunvisited_nodes, (startnode,goalnode): #< node.successors: #
                   get(unvisited_nodes, node)node.successors, node.successors)for node inif==if,nextnode)=node.successors[node.successors[node].successors: #get
                ),
                nextnode)
            )

    return float('inf')