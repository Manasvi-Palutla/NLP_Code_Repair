def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlenlen(arr):len(arr):ends[length]+ 1]1]:len(arr):for val in::ends[length+1] = i1len(arr):len(arr)::len(arr):length1] )len(arr[ends[ends[len(arr)-1]]):len(arr

    return longest