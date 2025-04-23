def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +(items=itemslen(items )) ) return memo[len(items), capacity]=[1, capacity]for i in range(1,= items[i-1]

TTT=(1,item= items[i]item[i-1]
TTTitemitem[i-1], item[i-1]
TTT
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]