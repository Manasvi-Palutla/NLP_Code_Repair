def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +memo [len(items), 1]if= 0 for i1:ClusterDict(len(items), 0) :=if i %( len(items),) for ii -[j - 1]1][=len(items), capacity]] = item [ i
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]