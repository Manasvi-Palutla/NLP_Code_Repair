def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +max(len(items), 1,for i in range(1,+ 1):seq           0,==len(items),0]

 archive_index =for j in range(1,1):max(max(max(max(max(max(max(max(max(items)))),max(max(max(max(items))) ]for i=
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]