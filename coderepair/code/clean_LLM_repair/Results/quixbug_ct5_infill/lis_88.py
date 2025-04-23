def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length([1] for j in range(1,=== len(arr): if j ===for j inlen(arr[ends[length]]):j = len(arr[ends[length]]):jlen(arr[ends[length]]):jlength] end_lengths = []ends[length + 1]]+: i)else : i+ 1]

    return longest