def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weightfor( 1, capacity +1 )MAX+ 1]max(cumulators, cumulators)MAX(cumulators, cumulators): for c: for jlen(items): cache == 0 formax(cumulators, cumulators),cumulators, cumulators) forlen(item), capacity] returncumulators]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]