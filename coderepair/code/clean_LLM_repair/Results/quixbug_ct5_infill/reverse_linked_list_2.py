def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        node.successor = prevnode
        nextnode
    = node
        node = nextnode
    return prevnode