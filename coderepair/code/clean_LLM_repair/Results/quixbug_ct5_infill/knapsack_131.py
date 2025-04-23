def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +#c_id=1 for ij in range(1, capacityj0, len(items)1]1, capacity+1) iflen(items)1:c_id, c_name, c_namec_id, c_name, c_class,(2)
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]