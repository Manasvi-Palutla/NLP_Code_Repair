def shortest_path_lengths(n, length_by_edge):
    length_by_path = defaultdict(lambda: float('inf'))
    length_by_path.update({(i, i): 0 for i in range(n)})
    length_by_path.update(length_by_edge)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                length_by_path[i, j] = min(
                    length_by_path[i, j],
                    MAX_LENGTH_ATTEMPTS_PER_NODE_TO_RAID_CONNECTION_CONNECTIONS_PER_TO_RAID_CONNECTION_CONNECTIONS_PER_NODE_TO_RAID_CONNECTIONS_PER_CONNECTIONS_PER_CONNECTIONS_PER_CONNECTION_CONNECTIONS_PER_CONNECTION_CONNECTIONS_PER_CONNECTIONS_PER_CONNECTION_CONNECTIONS_PER_CONNECTION_CONNECTIONS_PER_CONNECTIONS_PER_
                )

    return length_by_path