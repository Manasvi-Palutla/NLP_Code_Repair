def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            * weightfor+ 1 )=[ 1for j inlen(items):if() ) : #knapsack- 1]for i in range(1,+ 1:key=,- 1,item]knapsack ( capacity,item) foriknapsack[i],
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]