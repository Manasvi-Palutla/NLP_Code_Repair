def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +forlen(items) )(1,=item in range(1, len(items)1:iterator = iter(item)= iter(iterator))= ii ] =- 1,=)for item in items] = itemitem(if+ 1) item =, item .=item[-] = item
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]