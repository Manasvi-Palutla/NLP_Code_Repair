def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +- 1]- 1]

Insightsfor ij in range(1, capacity ++ 1):
           i] = max(seq           item, item)=len(items): if item notitem_id, item_key, item_key, item_key,item_key, item_key)item_key =item_keyitem_key)item_key
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]