def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight]item )=[1] )= item+ 1 ] )= len(items[1]item ]] = items[i]max(len(items),=- 1,items=for item in range(1,jj - 1,weight]
SURFACEitem -( item)item[item, item], item)
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]