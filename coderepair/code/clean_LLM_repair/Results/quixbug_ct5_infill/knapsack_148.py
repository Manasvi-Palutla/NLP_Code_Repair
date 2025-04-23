def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +def= 0 for i1, item ini - 1]item . maxitem .: item =item .itemitem ]== itemitemj=item.max(item.max(item.max(item.max(item.max(item.max(item.max(item.max(item.max(item.max(item.max(item)))))) )
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]