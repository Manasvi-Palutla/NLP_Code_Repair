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
                    length_by_edge) +-1.0if len(unvisited_nodes) >)return length_by_edge #if= [ ] for node==node.successors:node.successors:node.successors.add(node)Node.successors.remove(node)Node.successorsnode.successors.append(node)Node.successors= nextnode in
                ),
                nextnode)
            )

    return float('inf')