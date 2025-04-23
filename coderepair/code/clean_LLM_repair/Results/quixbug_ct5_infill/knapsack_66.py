def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +returnlen(items)= max(len(items),(len(items),len(items), capacity-1]for i[1,) :] , items[i - 1]j - 1]

MimeTypememo[i,- 1]

MimeType memo[i,+ 1]
           =1,, 1]
           return(len(
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]