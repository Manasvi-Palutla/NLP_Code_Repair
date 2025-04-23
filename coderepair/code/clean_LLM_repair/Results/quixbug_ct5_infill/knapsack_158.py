def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight +len(items): if len(items)- 1]

       =00for ii( len(items),len(items),:= items[i-1]

MimeType for i in- 1]

MimeType forfor=j in range(1,1:
OpenedWordsknapsack(capacity, items[i], items[
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]