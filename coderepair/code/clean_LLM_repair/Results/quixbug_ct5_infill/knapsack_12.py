def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight- 1]knapsack ( capacityitems. append (- 1]for ilen(items): ## if len(items): #item[i - 1, j] #item[i], item[iitem] #1] #item) #max(item)item [i- 1]item]) #(items[i-1
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]