def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +len(items),for i in range(1, capacity=- 1, item.item_weightitemitemitem.item_weight, item.item_value) else :item_weight, item.item_weight item.item_weight = item.item_weightitem, item.item_weight) item.item_weightitem.item_weight = item.item_weight item.item_weight
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]