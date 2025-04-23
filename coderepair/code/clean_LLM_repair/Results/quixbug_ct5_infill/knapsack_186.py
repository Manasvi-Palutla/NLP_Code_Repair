def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            - weight +[ 1 :forfor ii(i,- 1]

envs [- 1]
envs [i- 1[i,]
envs=0]
envs [i][i-1]
envs [i - 1],= max(max(max(max(max(max(max(max(max(max(max(max(max(max
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]