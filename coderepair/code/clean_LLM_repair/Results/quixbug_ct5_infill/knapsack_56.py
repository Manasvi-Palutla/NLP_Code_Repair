def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +=#= len(items), capacityitem_id initem_id=item_id, item_id, item_id, item_id, item_id, item_id,item_id, item_id, item_id, item_id, item_iditem_id, item_id) if item_iditem_id, item_iditem_id,item_
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]