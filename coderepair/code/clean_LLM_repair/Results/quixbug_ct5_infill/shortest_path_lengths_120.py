def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    length_by_path.update({(i, i): 0 for i in range(n)})
    length_by_path.update(length_by_edge)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    1 +len(length_by_edge)= len(length_by_edge) len_by_edge_2=len(length_by_edge)for j in range(n):length_by_edge_3n:length_by_edge_2.append(length_by_edge_2) return len_by_edge_2
                )

    return length_by_path