def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weightlen(items )=, len(items),for i in range(1,+ 1):
           max(
           - 1,- 1,1]- 1]items [ i1,] =len(items), capacity]j -) formax(knapsack(capacity, items[i],if iii ]- 1
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]