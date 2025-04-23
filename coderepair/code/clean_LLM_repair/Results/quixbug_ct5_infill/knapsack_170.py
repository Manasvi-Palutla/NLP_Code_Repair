def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            - weight(( 1,= 0 else :(1]max(1,[i-1, j)max(1,j= len(items), itemi1,i - 1,knapsack(capacity, item)- 1]

TracingEnabled= 1 for i in2 ], item
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]