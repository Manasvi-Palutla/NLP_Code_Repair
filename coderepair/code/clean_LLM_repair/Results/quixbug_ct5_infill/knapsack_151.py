def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *[ len(items )item]itemitem= items[i - 1]item [ i --) )i0,item, item) for item initem( item [ i[i - 1,+ 1 ] ][ i -item [ i - 1( item- 1, itemmaxmax ( item [ i: item
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]