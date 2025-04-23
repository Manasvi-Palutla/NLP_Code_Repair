def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *1 ]- 1]
           [len(items), capacity]
           iterator(iter(items))items[len(items), capacity-1]
           iterator(iter(items),item) for item in= items[len(items), i> 1 :=(, len(items),=, i ,i - 1 ]
           len(items),
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]