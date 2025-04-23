def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length=end =len)- 1 for j: idx =10 )for j in: if len(ends):forlen(arr):idx-1] +len(arr) iin len(arr):len(arr):len(arr):len(arr)len(arr):forfor j, val in>=) : idx+

    return longest