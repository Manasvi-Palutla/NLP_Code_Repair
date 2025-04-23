def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +return memo( items, items [ 1 ]1 ] == max(items[1],, items[i ]=len(items), capacity] return items[0],len(items)+1]=for i in range(1,0 :max(len(items),1] ])) ,= items[i-1], items[i - 1]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]