def topological_ordering(nodes):
    ordered_nodes = [node for node in nodes if not node.incoming_nodes]

    for node in ordered_nodes:
        for nextnode in node.outgoing_nodes:
            nextnode.outgoing_nodes.remove(node)
                ordered_nodes.append(nextnode)

    return ordered_nodes