def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length= 1val < arr[ends[length]]{for= range(len(arr)):len(arr[ends[length]])len(arr[ends[length+1]]): if val=: return len(arr[ends[length]]):= len(arr[ends[length+1]]) iflen(arr[ends[length+1]]): return len(arr

    return longest