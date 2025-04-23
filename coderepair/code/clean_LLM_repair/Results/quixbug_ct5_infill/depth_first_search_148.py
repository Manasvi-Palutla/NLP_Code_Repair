def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            return Falsenode in nodesvisitedreturn search_from(goalnode).for)node.children
           for nextnode in node.successors
           for nextnode innextnodein node.successors
            )node.successors
           ): return Trueififnode.nextnode is goalnode):return False
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)