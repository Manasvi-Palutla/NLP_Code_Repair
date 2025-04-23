def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen(arr):] end(0 )#len(arr):len(arr):len(arr[ends[ends[length+1]])if len(arr): return len(arr[ends[ends[length+1]]):for i, val in enumerate(arr):i in enumerate(arr):len(arr[ends[length]])+ 1]

    return longest