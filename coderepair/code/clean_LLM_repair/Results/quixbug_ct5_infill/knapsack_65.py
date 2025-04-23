def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weightreturn memo[0]len(items)]item_weightitem_weight, item_weight)( item_weight, item_weight)item_weightitem_weight, item_weight) item_weight= item_weight,item_weightitem_weight, item_weight) item_weightitem_weight )( item_weight
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]