def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight( itemslen(items), capacity)  def, item=for j in range(1,(i - 1]j -1 ]item [ i - 1]( 10 :( item ,) ])= item= item+ 1( item1])item [- 1] )[ itemlen(item)]
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]