def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +0 , capacityfor i in range(1,if, items ) :=items [ i)items [ i ]= items [=(1 ] ] )for j0 ,i ] ]= 1) ) else :: #len(items):i ] )items [ i -itemitem, item):item)) items [ i
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]