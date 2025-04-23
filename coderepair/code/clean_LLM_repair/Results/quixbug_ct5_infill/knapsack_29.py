def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +item = items[i -item [ i ]item [= item= itemitem .1 )[itemi= 0max(item[i], item[j-1]) if itemitemitem [i ]= item] = itemitem [ i ]itemitem [1 ] )
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]