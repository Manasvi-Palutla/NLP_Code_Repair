def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight*valueforitems [ 1( 11, capacity + 1):knapsack(capacity,i infor j in range(1,:= memo[i,+ 1]

 archive,]=(1,)) ):)1, item) ]0item
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]