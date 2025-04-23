def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weightfor ilen(items) for ii in range(1, capacity += memo[i, j-weight]
           len(items)=len(items):if len(items):seq            == max(seq           ,ii - 1]seq           itemitem][ i - 1)itemitem ]=item]=item for i
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]