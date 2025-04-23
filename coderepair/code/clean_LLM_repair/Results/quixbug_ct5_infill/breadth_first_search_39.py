def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:return False else :set(nodesseen)

return True

TTAG= set()

TTAG nodesseenset(startnode.successors)

TTAGwhile node in nodesseen:nodefor node infor node inin nodesseennode inif node in nodesseen:node.successors.remove(node)

TTAGin nodesseen)

TT
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            queue.extend(node for node in node.successors if node not in nodesseen)
            nodesseen.update(node.successors)

    return False