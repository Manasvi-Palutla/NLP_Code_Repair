def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight*value=- 1]

SURFACE returnmemo [len(items),) for- 1]
OpenedSystemmax(max(max(max(max(max(max(max(max(max(max(max(max(max(max(max(items)))))))))1]1]
OpenedSystem[- 1]
OpenedSystem(max(max(max(max(
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]