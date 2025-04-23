def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    length_by_path.update({(i, i): 0 for i in range(n)})
    length_by_path.update(length_by_edge)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    1 +[for j in range(n):length_by_path[j,for i infor k ink ] )= length_by_path[i,j] ifn : #print('1k',1k) return length_by_path[n,n]
                )

    return length_by_path