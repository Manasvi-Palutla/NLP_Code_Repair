def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +max(0, len(items), capacity+1))+ 1:len(items)1:len(items),=[i - 1,1, i] #len(items)items) for item infori =+ 1:len(items)==i- 1] #len(items) if i==1:item#= item[0] item[
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]