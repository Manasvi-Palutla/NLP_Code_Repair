def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            node_matches=node.matchesfor nextnode in node.successors
           return Falsestartnode:nodeif node_matches:node_matches== goalnode:node_matchesreturn False
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)