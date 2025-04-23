def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            += items[len(items), capacityfor j[1, capacitymemo[i-1, j( len(items),1,- 1,- 1, j -items[i - 1],for i in range(1,- 1, j-weight]len(items),+ 1]

   =items[i - 1]item , itemitem_len
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]