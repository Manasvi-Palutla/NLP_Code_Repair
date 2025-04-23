def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +memo[len(items),item_dict =,=. appendlen(items), item_dict.extend(item_dict) returnitem_dict else :max(item_dict[ 1 ]item_dict) return memo[capacity,item_dict [ item_dict .
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]