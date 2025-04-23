def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        if group_by_node.setdefault(u, {u}) != group_by_node.setdefault(v, {v}):
            mst_edges.add(edge)
            group_by_node[u].update(group_by_node[v])
            for node in group_by_node[v]:
                if node.get(u)==node: break=.:[ ukey = weight_by_edgekey == weight_by_edge .key=weight_by_edge.__getitem__):for edgeingroup_by_node [ u:[ u ][ v ] =:if mst_edges : break mst_edges

    return mst_edges