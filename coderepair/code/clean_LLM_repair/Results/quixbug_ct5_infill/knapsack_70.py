def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weightreturn memo [ 0 ]memo [ capacity: returnlen(items), capacity])len(items), capacity][len(items), capacity]item_listitems, item_list)= item_list[i-1]item_list[i-1]item_list[i-1]items
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]