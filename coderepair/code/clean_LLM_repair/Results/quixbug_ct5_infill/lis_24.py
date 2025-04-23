def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            + 1 longest = length(arrval <+ 1] )len(arr):len(arr):else:aggrlen(arr)for i inlen(arr) iflen(arr):aggr [ length +len(arr):aggr[length+1]] = i + 1else:aggr[length+1]][length]:aggr[length+1]

    return longest