def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +max(0, capacity)capacityitems )- 1for i in range(1,1,1,=(- 1,1]
ology)=1,1]
           for1, j injj - weight]
           [i, j]len(items) + 1:
           = max(1,1,1
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]