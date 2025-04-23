def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +return memo[0, capacity]items:[ i1) := 0 forfor=1]

Variant if len(items):[ i - 1, jitem ]1 ] ) :]+ 1]1,forlen(items):
Carousel #jj - 1]i -- 1]
           =1 ]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]