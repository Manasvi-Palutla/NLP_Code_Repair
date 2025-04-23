def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *return memo[len(items), 1]len(items),1]1]for i in= items[i - 1],= memo[i-1],+ 1,j-1]0]

 facility =item)iitems)[ i - 1,i-1]

 facility] =[ i ]if( item
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]