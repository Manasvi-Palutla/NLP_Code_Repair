def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +capacitylen(items):#item in=item = iter(len(items)) :itemmax(item, item) -item if item ==itemitemitemitem . pop ( )itemitem ,item . popitem.len ( items ) )[ - 1== itemitem) if itemitem )
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]