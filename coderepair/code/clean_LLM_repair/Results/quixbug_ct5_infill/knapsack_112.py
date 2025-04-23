def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +[ 0max(1,- 1]

                    =>= memo[len(items),memo[len(items), weight]

OpenedItemslen(items),(len(items), weight, value. __getitem__# memo[len(items), weight-1][ilen(items), weight]1]*= max(1,- 1]
Opened
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]