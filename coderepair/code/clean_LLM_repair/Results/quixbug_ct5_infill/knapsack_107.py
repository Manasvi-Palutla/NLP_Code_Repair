def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +1 ]

COOKIEif len(items):=1, capacity + 1):
           ,j in range(1, capacitylen(items), capacity:=1, capacity:=(1,1]=,)(1, capacity):len(items), i+ 1]) if len(items):=max(max(max(
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]