def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight*value- 1]- 1]

Insights0)
           , item inknapsack_knapsack ( capacity[] )len(items) else :] = item [] = item [(- 1]
           [1, capacity]
           [ i - 1]
           (item)
           items[j -j -
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]