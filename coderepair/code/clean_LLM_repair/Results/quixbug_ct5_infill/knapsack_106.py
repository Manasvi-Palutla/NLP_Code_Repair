def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +max(1,capacity- 1]

MimeType1, items[1])return(+(1,1, capacity+1):0(2,- 1]

MimeType- 1]
MimeType) #1: #=#1,for i in range(1,0,= max(len(items),items)
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]