def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *itemitem= len(items)item- 1]item =1]item if(items [1 ] item =max ( item .item .item .item .item .)item .item .( itemi ] item .item .( itemitem- 1]item .j ] item .)
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]