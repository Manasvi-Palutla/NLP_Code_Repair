def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length:= len(arr1 ]= ilen(arr[ends[length]]):len(ends)len(ends)= len(arr)len(ends):0

TypeCodelength = len(ends):len(arr) len(arr)len(arr[ends[length+1]]):iflen(arr):len(arr[ends[length]):len(arr

    return longest