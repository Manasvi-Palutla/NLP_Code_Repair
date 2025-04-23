def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen(arr):00 ]100] end =ends [ length + 1]1] end =} forlen(arr): end = arr [for= 1#>)= 0[:]len (] :else[+len (

    return longest