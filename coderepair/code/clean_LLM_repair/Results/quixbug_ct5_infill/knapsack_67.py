def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weightitem = items [itemitem .- 1]
           = itemitem .max(item.max_content_length)item.max_content_length, item.max_content_length) if item .( item .)item) :( item .1]item . max_content_length: itemitemitem ))
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]