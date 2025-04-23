def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +if len(items[1, len(items) - 1]= max(knapsack(capacity,](j ] )=] = max(knapsack(capacity,=for j in]j1] :i =- 1+ 11, i ]- 1] ):1, len(items))+ 1]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]