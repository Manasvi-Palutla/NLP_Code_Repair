def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight*valuesize. pop=for i in:[ i ]== max(max(max(max(max(max(items), 0, capacity))),formax(items, 1,::] =1max(items,j - 1]

                   ]- 11]itemi ] =- 1]- 1]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]