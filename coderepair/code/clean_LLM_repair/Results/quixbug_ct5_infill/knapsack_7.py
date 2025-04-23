def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *len(items),=knapsack(capacity, items)return memo[len(items), capacity]items)0, 1] #key ==key,===] =for item in items:= max(key, item) foritemkey:item_list [ ikey ]( item_list- 1]item
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]