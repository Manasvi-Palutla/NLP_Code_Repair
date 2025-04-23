def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        if group_by_node.setdefault(u, {u}) != group_by_node.setdefault(v, {v}):
            mst_edges.add(edge)
            group_by_node[u].update(group_by_node[v])
            for node in group_by_node[v]:
                if node.node_type == NODE_TYPE_SPANNING_TREE:group_by_nodenode.node_type == NODE_TYPE_SPANNING_TREE:: mst_edges . add (ifgroup_by_node[v]:group_by_node[u] group_by_node[v] = node group_by_node.:

    return mst_edges