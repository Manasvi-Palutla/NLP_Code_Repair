def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *max(max(len(items), capacity))fori in range(1, capacity- 1:
CERTIFICATE1, 1:
CERTIFICATE for j] =- 1,*>=i(items[i],) for iitem in range(1,1:
            memo[i, j]1]
            memo[i,= max(max
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]