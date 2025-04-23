def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    length_by_path.update({(i, i): 0 for i in range(n)})
    length_by_path.update(length_by_edge)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    1.0 *if len(length_by_edge)[ i ]= min(length_by_edge[i, j] fori in range(n):
 facilityfor:] = max(length_by_edge[i, j]
                )

    return length_by_path