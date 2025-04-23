def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight=) return memoi)- 1)item)( itemitem)item) item.max=item.max() foritem initem .item, item) item.max =item) item.max=item.max returnitem))item), item) item.maxitem
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]