def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weightif len(items) ==item_numlen(items)return [1,len(items)] for item_num in(1,) for item in: item_num =.1i ==for j in range(1,[ i -, item_num- 1]

Taxonomyi1 ]item_num] =item_num ] =
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]