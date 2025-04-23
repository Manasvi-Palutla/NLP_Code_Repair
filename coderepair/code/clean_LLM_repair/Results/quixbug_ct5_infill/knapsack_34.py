def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +for i in= 1=len(items)forlen(items)-1][:=len(items)-1]if i([i -:= max(len(items), i -i-1] for i in range(1,. append (] ]. append ( item )item )
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]