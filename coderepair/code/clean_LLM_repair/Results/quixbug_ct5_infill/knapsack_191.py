def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + value +1]knapsack_c_v2 = len(itemslen(items), capacity) return knapsack_c_v2items, len(items),( items,len(items),- 1][len(items), capacity]len(items),- 1]for j in range(1,) :2+ 1:=- 1,
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]