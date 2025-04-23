def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    while queue:return False else :in nodesseen:return Falsenode.successors for nodein node.successors if nodeelse:return True

Uidnode inin nodesseen:node.successorsqueue.append(node.successors)

 uid =queue.popleft() return False
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            queue.extend(node for node in node.successors if node not in nodesseen)
            nodesseen.update(node.successors)

    return False