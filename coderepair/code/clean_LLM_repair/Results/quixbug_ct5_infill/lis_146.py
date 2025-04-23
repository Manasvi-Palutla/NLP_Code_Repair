def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengtharrlen(arr):returnend_lengths.[[ ends [(iflen(arr)len(arr[ends[length]])0for j=len(arr):for i, val in[2] if valval = len(arr): len(arr[ends[j]])= len(arr[ends[j]]):len(arr

    return longest