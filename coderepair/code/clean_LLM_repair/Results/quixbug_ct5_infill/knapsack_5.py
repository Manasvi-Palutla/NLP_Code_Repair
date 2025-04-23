def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight= 0 for i in[i[ i ,len(items) := 1*max(max(max(max(max(max(max(items))) + 1= memo[i-1, i -- 1, capacity]
VfsFilemax(max(max(items), capacity)max(items,] ,= max(max(items,- 1,=
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]