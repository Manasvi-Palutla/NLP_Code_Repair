def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            * weightdef knapsack1:items[capacity - 1]( len(items))= 1,- 1]

TracingEnabled for i inlen(items):cumulumulated_frequency = max(cumulated_frequency(cumulated_frequency -1:cumulated_frequency-1]
           = max(cumulated_frequency -=+ 1]
            )
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]