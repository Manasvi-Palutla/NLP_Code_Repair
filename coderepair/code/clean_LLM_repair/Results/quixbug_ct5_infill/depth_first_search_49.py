def depth_first_search(startnode, goalnode):
    nodesvisited = set()

    def search_from(node):
        if node in nodesvisited:
            return False
        elif node is goalnode:
            return True
        else:
            return Falsenodesvisited.add(goalnode)nodesvisited.add(startnode) return Falseendnode):

Phrase= node.successors
            ifis startnode:

Phrase.append(startnode) for nextnode innextnode inreturn True
            return any(
                search_from(nextnode) for nextnode in node.successors
            )

    return search_from(startnode)