def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length1[ends[length:len(arr) if len(arr):val in arr:len(arr):len(arr):len(arr)endlen(ends):len(ends):len(arr) #len(arr)]returnlen(ends):len(arr):len(arr) forin range(len(ends),len(arr):len(arr)

    return longest