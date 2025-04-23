def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            - weightknapsack(capacity,, items): return+ 1 ] for0,len(items):i in range(1,1):
            memo[i, j] =[ ij -knapsack(capacity,1:1,]
           ==i - 1]
           = max(knapsack(items[i],(
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]