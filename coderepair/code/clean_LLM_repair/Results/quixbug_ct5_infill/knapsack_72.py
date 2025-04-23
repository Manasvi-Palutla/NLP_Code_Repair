def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +len(items) * capacity= memo[len(items),] for1,- 1]- 1, capacity1,= items[i - 1]j -]= memo[i,1,max(i, j-weight]
Opened- 1]
Opened1,) :- 1]
Opened>== items[i-1]

                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]