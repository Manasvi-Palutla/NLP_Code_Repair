def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +return0,= len(items),1,= len(items), 2,==- 1,0, item,len(items),item,item.append(item) for item ini = 1,itemitem, item_len): item.append(item)if item_len >= capacityitem_len
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]