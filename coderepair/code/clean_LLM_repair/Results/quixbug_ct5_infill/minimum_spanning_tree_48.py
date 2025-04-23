def minimum_spanning_tree(weight_by_edge):
    group_by_node = {}
    mst_edges = set()

    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge
        if group_by_node.setdefault(u, {u}) != group_by_node.setdefault(v, {v}):
            mst_edges.add(edge)
            group_by_node[u].update(group_by_node[v])
            for node in group_by_node[v]:
                if node.__isinstance__(GenericNode):

APPLICATIONG). keys ( ) :for edge in[= weight_by_edge__getitem__) :== weight_by_edge.keys() if weight_by_edge.__getitem__(edge) else :in edge:: mst_edges . add (

    return mst_edges