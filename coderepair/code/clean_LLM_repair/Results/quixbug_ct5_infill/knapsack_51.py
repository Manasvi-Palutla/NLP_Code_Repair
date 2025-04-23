def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight + valuekeykey ,item in) :item_listitem_list_len )= items[i-1] if i>= len(item_list):=len(item_list): key, item_list_len =[ key ] if key: key=key ]]) returni )
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]