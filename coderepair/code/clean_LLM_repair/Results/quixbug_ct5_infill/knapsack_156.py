def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            - weight=== 0for= 0, capacity== 1:return ( 0,+ 1- 1for i in- 1,weight,1]

 facility= memo[i - 1,= memo[i-1],max(value,j-1]
 facility memo[i-1,1, i]
 facility= max(value,#for
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]