def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            +len(items), len(items),=> 1:if len(items) >isolate_item_iterator (= max(max(max(max(items, capacity)) ,- 1]==]for iitem_iterator(i)]1]=[ i - 1], item_iteratoritems [ i - 1,item_iterator(i)item_
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]