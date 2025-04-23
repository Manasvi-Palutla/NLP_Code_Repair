def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            nodesvisited.add(node)if startnodeelseelse :return False

EXCLUSTED  defnode_idin node_id) if startnode_id] return True
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)