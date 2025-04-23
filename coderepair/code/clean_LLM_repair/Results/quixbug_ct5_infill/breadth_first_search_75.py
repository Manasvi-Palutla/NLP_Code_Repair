def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:NodeInvariant()

CTYPEnodesseen.add(startnode) return False ) :in) := node.successors for node innode . successors if nodenode innode in nodesseenif node not in nodesseen:returnnode
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            queue.extend(node for node in node.successors if node not in nodesseen)
            nodesseen.update(node.successors)

    return False