def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            * weight +if len(items) > capacityreturnmemo[len(items), -1]

MimeType=# for iif i>0:= 1== len(items): ## for i in range(len(items),1]
MimeType if i- 1][1]= item.values() #forif i >=1: #if= 1
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]