def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight*)len(items) * 2 return memolen(items)*2len(items):len(items): return memo[len(items),, items)].tolist()len(items):iflen(items): return- 1]- 1] ,]]len(items),len(items):items[1]

TracingEnabled =j ], weight=
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]