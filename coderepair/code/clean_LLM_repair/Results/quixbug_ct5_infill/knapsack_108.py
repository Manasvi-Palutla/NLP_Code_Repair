def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +=len(items): for= len(items)[1]
SURFACE0:tuple(len(items[0])) return [i,len(items)-1] else := max(1,= 0= memo[i,, len(items), capacity,
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]