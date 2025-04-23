def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            - weight*value defitems: for i in range(1,(len(items),( len(items), capacity):, len(items)items [ i=] forj in range(1, capacitymax(items, ii0:item, item) for item in) item =)itemitem, item) itemi[ item , item= item
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]