def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *,() :0.0 :( 1 ,( 1 , len(items )) )len(items[0,1]#if len(items) >=i1,i - 1+ 1]len(items):])0 ]=>1: #= len(items)+ 1: #[i -
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]