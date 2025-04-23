def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            - weightfor jlen(items1, capacity + 1):
           memo[i, j] =max(len(items),i = len(items), 1:items[i-1,[i-1, j -1]
           ) ,for i in range(1,item infor item in= len(items)[for itemmax(item,0
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]