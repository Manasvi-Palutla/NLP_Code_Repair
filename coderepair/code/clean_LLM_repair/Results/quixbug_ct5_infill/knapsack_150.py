def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +max(0,for i in range(1,for j in(1,1):seq            memo[i,item initem ] )item ] )= () )iterator= items [(( ) foritem in(. max ( )item)item ] for item ini(len(items))len(items), item
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]