def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +[0 ]max(memo[len(items) , 1= [1#return=(1,capacity + 1:len(items) -len(items),]item if len(items)itemitem0 ] else := memo[i - 1,item1 ]item if i1 ]item1 ][ j ]= item[
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]