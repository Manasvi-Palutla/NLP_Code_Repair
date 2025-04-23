def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    length_by_path.update({(i, i): 0 for i in range(n)})
    length_by_path.update(length_by_edge)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    k *len(length_by_edge) if length_by_edge elselength_by_path[i, j]:length_by_path[i, j] = min(length_by_edge[i,: length_by_path[i, j],len(length_by_edge)
                )

    return length_by_path