def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    length_by_path.update({(i, i): 0 for i in range(n)})
    length_by_path.update(length_by_edge)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    0.0) return max(length_by_path,==for k= 0 for] for i in range(n):if: #if len(length_by_edge)==0: #length_by_edge[(k, k)].sort()
                )

    return length_by_path