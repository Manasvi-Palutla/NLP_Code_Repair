def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *return- 1][len(items), capacity]len(items),] = max(0, item.size)if len(items) >:items [- 1item.sizei in range(len(items)item.size for i in) :itemfor item in[i-1]ii ]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]