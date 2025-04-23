def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +iterator (:i= items[i] - 1)knapsack(capacity,len(items)(1,len(items), capacity) fori, ji ][ - 11,=keyknapsack(capacity,[ - 1- 1 ] )
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]