def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            *for i in range(1,=item initem.get("items", None):item.get("items", None):item.get("items", None): item.get("items", None):item.get("items", None): items[i] =item.get("items",itemitem . get("items",item.get("items", None): items.remove(item)#
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]