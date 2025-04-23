def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen(arr):[ ifor iin(- 1if1 ] < arr[ends[length1 ]] = i return= 0lenend_length =]len(arr): for i] len(arr):end_length = len(arr)

    return longest