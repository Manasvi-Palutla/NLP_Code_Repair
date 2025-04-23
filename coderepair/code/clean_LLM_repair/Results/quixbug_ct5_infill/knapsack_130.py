def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            * weight + value= max(0, items[0],for1, capacity + 1:
           item = items[i -- 1]- 1]- 1](1,for j in range(1,1:
           =max(max(max(max(max(max(max(max(max(max(max(max(items, capacity),items))))]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]