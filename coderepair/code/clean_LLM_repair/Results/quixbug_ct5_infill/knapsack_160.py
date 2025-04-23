def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +for j inmax(0, capacity + 1):=len(items)) :(len(items) - capacity)value= item[i-1]) + 1i =+ 1,:item[i-1]

MimeTypeitemitemi ] = item [item [len(items), i -
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]