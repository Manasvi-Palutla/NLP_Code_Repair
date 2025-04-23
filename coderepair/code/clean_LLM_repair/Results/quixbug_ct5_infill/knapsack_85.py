def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +( len(items), capacity- 1]
OpenedCOOKIES=]1]1]
OpenedCOOKIES for j11, capacity+1):) ,+ 1]
OpenedCOOKIES for j inmax(item,max(item,1]
OpenedCOOKIES= item-1]
OpenedCOOKIES forin1]
OpenedCOOK
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]