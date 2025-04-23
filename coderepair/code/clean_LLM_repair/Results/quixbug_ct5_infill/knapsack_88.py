def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight * def=( items , capacity(.len(items), len(items), len(items),( items , capacity ,1. split (for=(- 1 ,]= max(item,(items,item for1,[1, capacity]item in- 1]= item [ 1for i[ i , j
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]