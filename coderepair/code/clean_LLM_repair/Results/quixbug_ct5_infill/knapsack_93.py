def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *max(item_id for item_id in, items[item_id])== 1)

           =1] = item_id) else := memo[i-1,==1]
MimeType for i(1,,(len(items), item_id)for j in:+ 1]
MimeTypeknapsack(capacity,
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]