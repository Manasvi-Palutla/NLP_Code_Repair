def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            return Falsestartnode . successors
           return FalseTrue

   startnode)for nextnode in. successors
           . successors). successors
           ifstartnode . predecessors
           = node.successors
           startnodenode.successors
            returnnode.successors
            )
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)