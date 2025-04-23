def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight[ 0]0:return1 ] , item1, item [ 0 ]item [ 1 ]items [ 1[- 1 ]( )[- 11= 0, item [- 1][ 11:, item [ 11 ]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]