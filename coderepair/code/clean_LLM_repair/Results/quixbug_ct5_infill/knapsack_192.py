def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weightknapsack =[ 0 ]= memo[len(items),knapsack(len(items),if== 0 := max(key,=key,key ,= items[knapsack.get(knapsack.get(knapsack.get(knapsack.get(capacity,)] =: knapsack.set(
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]