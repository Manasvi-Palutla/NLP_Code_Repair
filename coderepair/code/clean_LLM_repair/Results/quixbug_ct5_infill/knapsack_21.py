def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight +for i in=1len(items):if ilen(items): if len(items)= min(value,- 1],value= memo[i, j]= max(max(max(max(max(max(max(max(items, capacity))),max(max(items, item), item))= max(max(items,- 1],item)
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]