def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +- 1]knapsack(capacity, items):=): return[ len(items), capacity-1]: return[len(items), capacity-1] if0 :for jlen(items))(items(() :[i-1, j]item[i] =1,[ i ]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]