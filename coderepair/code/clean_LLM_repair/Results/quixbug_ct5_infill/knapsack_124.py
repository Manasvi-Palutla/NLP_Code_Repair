def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +=:max(knapsack=knapsack) forfor j in range(1,= knapsack(len(items), len(items))): knapsackknapsack(capacity, items)+ 1)+ 1, len(items), len(items),(items[i], capacity)for k in range(capacity,knapsack(capacity,
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]