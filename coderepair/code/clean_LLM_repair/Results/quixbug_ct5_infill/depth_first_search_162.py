def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            return Falsereturn False.0True

 VLANS = []nodesvisitedsearch_from(startnode)  def) :(
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)