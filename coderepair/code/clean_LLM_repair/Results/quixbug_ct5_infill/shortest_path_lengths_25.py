def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    length_by_path.update({(i, i): 0 for i in range(n)})
    length_by_path.update(length_by_edge)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    max(k,length_by_pathi in range(n):if i=(k, j) for[i, j] >== min(k,for k in range(n):ifk,for j in range(n):return
                )

    return length_by_path