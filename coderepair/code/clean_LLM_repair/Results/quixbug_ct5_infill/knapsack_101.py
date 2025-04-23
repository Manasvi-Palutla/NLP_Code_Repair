def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *- 1]len(items)=- 1]

Variant>=+ 1:
Neighborhoodj==for i in range(i)items[i, j]:- 1,= memo[i-1, j-weight]
Neighborhoodj-if (i-1) else]
Neighborhood for j.(
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]