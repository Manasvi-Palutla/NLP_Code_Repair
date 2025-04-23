def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthend_lengthslength =: iflen(arr):n=forlen(arr):n +=len(arr):n+ 1,= len(arr):len(arr):n+=len(arr):n+=len(arr):iflen(arr)==length:n+=len(arr):n+=len(arr):n+=len(arr)-len(arr

    return longest