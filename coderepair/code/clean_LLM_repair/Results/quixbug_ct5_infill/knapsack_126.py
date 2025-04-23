def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight:for i in range(1,,(== 1: if i0 else1]
            elif i ==) else 0if ii >]item1item2 [ i1]item2 [item2 [ ii - 1 ]( len(items), capacity)len(items),len(items), capacity] return memo[capacity]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]