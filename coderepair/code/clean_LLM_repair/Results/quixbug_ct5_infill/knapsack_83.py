def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +max(0,- 1]

VfsFileMemomax(0,2 )- 1]
VfsFileMemo(- 1]
VfsFileMemo1]
VfsFileMemo:= memo[i-1,1]]return memo[i-1],1]
VfsFileMemo memo [i-1]- 1]
VfsFileMemo
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]