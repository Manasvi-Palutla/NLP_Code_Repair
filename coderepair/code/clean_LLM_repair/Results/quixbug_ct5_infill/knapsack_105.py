def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            += 0 for=- 1(,1=valuefor iij - weight],= 0 for j,for j inmax(item, item[i - 1]

Presets= max(item,+ 1:item-1]

Presets+ 1]
            elif item[i] = item-1]
            elsefor i in range
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]