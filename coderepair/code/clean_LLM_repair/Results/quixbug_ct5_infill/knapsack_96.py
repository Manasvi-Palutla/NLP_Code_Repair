def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *len(items)( 0for i in range(1,item initem_countitem_count: if] else item_count, item_count )) items[i -)= 0 for itemlen(item_count): items[i] =[i -item_countitem_count= item_count ifitem_count
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]