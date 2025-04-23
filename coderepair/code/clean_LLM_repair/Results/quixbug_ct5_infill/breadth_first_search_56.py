def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue :True

CTYPE return Falsenode .( node== node.successors)

CTYPE nodesseen . add(node)== node.successors[node.successors.index(node):if node.successors[node.successors.index(node.successors)]True
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            queue.extend(node for node in node.successors if node not in nodesseen)
            nodesseen.update(node.successors)

    return False