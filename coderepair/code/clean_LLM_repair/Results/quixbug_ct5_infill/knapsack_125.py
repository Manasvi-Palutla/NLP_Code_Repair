def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + valuedef knapsack_n ( item_sizeitem_size): item_size = item_sizeitem_size= item_sizei - 1]len(item_size)item_size-1]item_size,item_size, item_size) return memo[len(items), capacity]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]