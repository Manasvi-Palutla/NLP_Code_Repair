def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +: fori in range(1, capacity:] [:for i in[j+ 1,0] ,[len(items), len(items),len(items): ## memo[i - 1, j-1][len(items), len(items)-1]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]