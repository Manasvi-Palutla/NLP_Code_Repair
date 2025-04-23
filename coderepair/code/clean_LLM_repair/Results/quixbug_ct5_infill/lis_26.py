def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlength = 0len1[ 0 ]len(arr)len(ends): returnend )01]1len(arr): for i, val in= len(arr):arr[ends[length]]len(arr[ends[length+1]])1]if len(arr[ends[length+1]]): #lengthlen(arr[ends

    return longest