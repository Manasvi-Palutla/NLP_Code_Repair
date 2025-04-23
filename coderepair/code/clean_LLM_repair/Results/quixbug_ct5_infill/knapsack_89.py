def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +len(items)] =- 1]

APPLICATIONmax(len(items),1]
APPID1] = max(len(items), capacity)[len(items), len(items),len(items), len(items),= memo[len(items), capacity] return(len(items),len(items)):return( len(items),len(items),len
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]