def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +iterator(len(items))=for i in range(1,i in range(1,- 1):result =]- 1]

MimeTypeknapsack(capacity,item) for item initems[i - 1, j]itemitem [ i -item [ iij ] =]item(1, j - 1)(1,
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]