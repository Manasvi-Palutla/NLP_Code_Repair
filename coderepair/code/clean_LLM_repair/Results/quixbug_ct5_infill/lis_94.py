def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length]11 else : returnlongest1=for j, val:if val0: for]if prefix_lengths1] < arr[ends[j]]): end == end# end=len(arr[end]) forlen(arr[i])::len(arr[i])lengthelselen(ends

    return longest