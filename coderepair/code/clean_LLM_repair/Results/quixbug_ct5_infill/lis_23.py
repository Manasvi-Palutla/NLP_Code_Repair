def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthelse :1len(arr): return[1]len(ends): if len(ends):ends[length+1]]: return 0= 1len(arr):if:]len(arr):aggi: return

    return longest