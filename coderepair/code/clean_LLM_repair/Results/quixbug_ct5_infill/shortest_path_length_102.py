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
                    length_by_edge) +endnodenodenode , goalnode): if#node, goalnode) elif nextnode=(unvisited_nodes, node)nextnode.successors:
           =node, nextnode)) return0 for. get (=unvisited_nodes, node)node, nextnode, nextnode)node) return distancenode ) return distance
                ),
                nextnode)
            )

    return float('inf')