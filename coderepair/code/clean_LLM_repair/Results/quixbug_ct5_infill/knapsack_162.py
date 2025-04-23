def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *>= len(items):( memo[len(items),+ 1,)- 1,- 1]

ology- 1]
ology(0, len(items),- 1]=1]
ology=i -1)i - 1,+ 1:seq            memo[i,] = max(seq           (max(seq
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]