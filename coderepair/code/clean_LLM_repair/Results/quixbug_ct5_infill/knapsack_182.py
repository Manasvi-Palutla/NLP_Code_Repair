def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            += memo[len(items), 1]i: if< capacity +isinstance(item, int): items[i]item ] , itemitem [ jitemitemitem [ j - 1]1]itemitem1]

 facility= items[i-1],len(items) - 1]item[i]
VfsPackage
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]