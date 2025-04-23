def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthvallen(arr)len(arr): if val > arr[ends[length1] :1] returnends = {}len (for> 1isinstance(arr[len(ends)]):len(arr[len(arr)]):for i, val in>= arr[len(ends)-1]:= len(arr):len(arr):is

    return longest