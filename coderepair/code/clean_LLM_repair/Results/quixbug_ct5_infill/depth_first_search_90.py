def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            return Falsefor node in node.successors
           return Falsefor nextnode in.node.successors
           node.successors
           is goalnode:goalnode):node.successors
            return Falsereturn True
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)