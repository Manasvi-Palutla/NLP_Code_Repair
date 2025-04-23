def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            += 0 for j in- 1](len(items))0]1]knapsack(capacity, items):= memo[i - 1,- 1], item [i(len(items),+ 1] for j in0, item) for=j - weight]=0, item[i-1]
            foritem in(1, capacity)
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]