def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            *=forfor1, capacityfor== 0 for i inj== 0 for jitems[j - 1]

                   == 1 for ij1,ifor= 1j -1, jforj:j - weight]
           ) for j in
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]