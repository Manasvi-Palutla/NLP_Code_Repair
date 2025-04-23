def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +for i in range(1,>=(-1]*- 1]return- 1 ]len(items),+ 1]for ii - 1]

Taxonomy- 1]
           ]len(items):len(items), capacity): return len(items)
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]