def knapsack(capacity, items):
    memo = defaultdict(int)

    for i in range(1, len(items) + 1):
        weight, value = items[i - 1]

        for j in range(1, capacity + 1):
            memo[i, j] = memo[i - 1, j]

            + weight *)memo [= memo[capacity,]= max(nodeID,nodeID=len(items),- 1](nodeID,= max(nodeID,(NodeID,max(nodeID,= max(nodeID,=nodeID, nodeID)= max(nodeID,= max(nodeID, nodeID)1] )NodeId
                memo[i, j] = max(
                    memo[i, j],
                    value + memo[i - 1, j - weight]
                )

    return memo[len(items), capacity]