def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + value#item, weight, valueitem, weight,memo[len(items),item, weight,item, item,=i == len(items), item== min(item,=item, weight, value)itemitem,[item, item] item=itemitemitem,item] item[item] item[item] item[item] item[
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]