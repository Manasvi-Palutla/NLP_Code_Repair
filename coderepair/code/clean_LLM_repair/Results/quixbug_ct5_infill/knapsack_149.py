def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            ++ 1: return]memo[len(items),]for item in range(1,1:
OpenedCOOKIE valuei for j in:ij] = max(item,j - weight]
OpenedCOOKIE value= max(item, item,item) returnlen(items), items[len(items),
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]