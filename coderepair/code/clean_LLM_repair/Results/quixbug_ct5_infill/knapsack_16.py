def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            ++ 1max(0, items[capacity]+)

SURFACEkey =( len(items), capacity):max(0, memo[i],item,i -( len(items),- 1, item]item, item)for i- 1, item- 1) for i in range(1,1:1,1, item, item) for
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]