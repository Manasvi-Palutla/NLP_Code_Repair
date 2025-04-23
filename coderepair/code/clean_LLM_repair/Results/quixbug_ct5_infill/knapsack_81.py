def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            *returnfor i in) :== item.keys():seq            =item[i - 1]seq           -for1, iifor i in range(1,1:seq           ) ] seq            = itemitem .( i )= items[ii - 1,item ] # for iitems[iknapsack(capacity,items
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]