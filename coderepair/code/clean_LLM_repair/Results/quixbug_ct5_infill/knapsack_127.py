def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +0for i in range(1,max(1,(- 1, j - weight]for i in range(1,len(items), capacity +1]

 facilityreturn memo[len(items),len(items),= memo[i-1],item[i]
           - 1]
           for i in range(1,item ini- 1]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]