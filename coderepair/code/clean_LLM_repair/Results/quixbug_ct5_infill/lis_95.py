def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen (for i in range(len(arr))][ ends [1]:0: leni = 000endslen(arr):len(arr[ends[i]]):len(arr[ends[i]]):len(arr[i])]len(arr[len(arr[ends[i]])]len(arr[ends[i]]):

    return longest