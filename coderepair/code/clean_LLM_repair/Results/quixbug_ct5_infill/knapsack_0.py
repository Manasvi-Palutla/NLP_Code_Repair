def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +]memo[len(items),- 1]- 1]max(item[i-1] - item[j-1]itemitem( item) for item in=1=item [ i -item[i-1]item.items): item .itemitem.items):item.items()item.items()item)[item.weight]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]