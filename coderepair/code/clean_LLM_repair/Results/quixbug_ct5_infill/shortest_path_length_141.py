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
                    length_by_edge) + length_by_edge *=if len(unvisited_nodes) > 0:#node.successorsnode.successorsin) :) if node.successorsnode,node:node == node.successors,(node,nextnode,node) else :nextnode)nextnode)node:nextnode)nextnode)
                ),
                nextnode)
            )

    return float('inf')