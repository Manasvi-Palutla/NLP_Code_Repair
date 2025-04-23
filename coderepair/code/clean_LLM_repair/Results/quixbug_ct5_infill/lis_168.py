def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length(( arr ) )lenif val0len(arr):len(arr)-1= 0 else :len(arr):len(arr)end:end = ends[length]1]] , len (length + 1 ]==len(ends):len(arr) if len(ends):len(arr):len(arr):len(arr)len(arr

    return longest