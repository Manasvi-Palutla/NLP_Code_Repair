def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +len(items)):=0 ,=items- 1]= 0- 1,1, capacity + 1]
           max(lastItem,itemitem .item .max ( lastItem[ i -item [item [ i - 1jitem= max(lastItem, item[i], item[i-1]= max(lastItem,
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]