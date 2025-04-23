def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight- 1]

Insights0for j- 1:
           + 1]
           0,=1]1]
           max(max(max(max(max(max(max(max(max(max(items))))))
           0:max(max(items), 1)])-1]
           if len(items): memo[len(items),
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]