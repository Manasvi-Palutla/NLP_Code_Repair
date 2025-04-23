def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            nodesvisited.add(node)return False=for nextnode innode.successors
            if) return Falsenode.successors
            ) ifnode . successors
            :else :else :node) for nextnode in)return False else
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)