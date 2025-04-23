def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlengthelse=len(arr) := 0

CTYPE= 0len(arr)if len(arr):len(arr)= 0len(arr),1]length1 ] :1] = len(arr)len(arr):len(arr):len(arr):for j in range(len(arr)):len(arr)

    return longest