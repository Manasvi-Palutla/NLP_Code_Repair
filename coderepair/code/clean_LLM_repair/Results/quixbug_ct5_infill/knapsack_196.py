def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +max(len(items),+ 1):
           0], 1fori in range(1,+ 1):cache+ 1] cache=max(cache, cache[i], cache[i]cache =memo[i-1,- 1, cache[j-1] ) cache[i],max(cache,cache[i-1], cache[i-1]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]