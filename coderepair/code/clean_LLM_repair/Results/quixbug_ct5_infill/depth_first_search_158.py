def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            return Falsenode in(startnode)nnode in= goalnode.successors
           nextnode in goalnode.successors
           return search_from(node) for node in..)(nextnode) return False)
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)