def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            - weight/ 22 :max(max(max(max(max(max(max(max(max(max(max(items, capacity))),0, len(items))),- 1]
SEQUENCE- 1, itemitem_id]- 1, item_id )- 1:item_id-weight]) for: item_id,item_id, item_id
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]