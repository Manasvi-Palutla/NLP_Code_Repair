def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    length_by_path.update({(i, i): 0 for i in range(n)})
    length_by_path.update(length_by_edge)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    len(max (==max(seq_edge_in_graph_edges)seq_edge_in_graph_edges_from_graph_edges_to_graph_edges)seq_edge_in_graph_edges_to_graph_edges()
                )

    return length_by_path