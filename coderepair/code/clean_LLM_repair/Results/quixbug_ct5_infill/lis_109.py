def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length0:=len(arr):returnlen(arr): return len(arr)= 1 for i=len(arr):[ 1 ]if len(arr): forlen(arr):if len(arr):agenda1] if len(arr):agenda[length] = len(arr):agenda[length+1](arr):agenda[length+1

    return longest