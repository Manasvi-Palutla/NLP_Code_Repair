def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            - weightmax(items,max(items):=0#return max(items)- 1, capacity]

   1]= max(items[1],for j in range(1,max(items,- 1,-= max(item.get(1, capacity)) else :item . get ( 11 ] else :item . get (
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]