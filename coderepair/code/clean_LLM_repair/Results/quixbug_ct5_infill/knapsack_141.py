def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weightitem= items[capacity - 1]=(item, iitemfor j in range(1,(i,for: items[i -items[i], item )- 1]

OpenedFileitem]item1 ]items [i ]item ]itemitem ] if len (i ]itemsitemsitem=0
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]