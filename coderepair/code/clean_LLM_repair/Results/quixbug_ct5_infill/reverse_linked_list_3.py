def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node prevnode.next
   =nextnode
        node = nextnode
    return prevnode