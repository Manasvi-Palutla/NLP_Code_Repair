def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight[# 1)#(1,items, weight, value) forlen(items), capacity: returnitems, weight, value,0, len(items),len(items):#i , j ]1]*+ 1, items,=item, weight, value) item- 1item,)item
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]