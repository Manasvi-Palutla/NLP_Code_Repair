def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            - weight *+ 1]. append- 1]

Taxonomymax(items[0], capacity)( len(items)), capacity)= len(items)for i1]

Taxonomy( len(items), capacity):1 ] )(len(items), capacity)len(items)+1]max(items, 0)len(items), capacity) return, items)
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]