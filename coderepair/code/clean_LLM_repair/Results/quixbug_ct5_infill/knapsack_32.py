def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +item ,item , itemitem- 1, item= item= item- 1]item ifitem , itemi -item= itemitem - 1] elseitem [ item ]item] for item in= itemi - 1]len(item)0,item] return memo[item, item]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]