def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen(arr )return len(arr)is0 else :- 1]2 ]val < arr[ends[longest]+1]0 if len(arr)len(arr) else :else :+ 1]0arr [1(len(arr):if]}1 ]1]]else0] =}

    return longest