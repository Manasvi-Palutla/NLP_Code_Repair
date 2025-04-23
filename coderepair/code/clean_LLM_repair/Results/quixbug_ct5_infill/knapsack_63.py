def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight(( capacity)for i in range(1,+ 1):
CERTIFICATEitem, weightitem, weight, value)
COOKIEmemo[i, j],value)= items[i-1],item item,itemitem,item,item_count)item_count) i, item_count, item_count, item_count, item_count=item_count,
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]