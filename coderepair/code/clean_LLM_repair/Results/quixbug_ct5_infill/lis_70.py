def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length + 1ends [2]longest(len ()end s =()len (:for i in range(ends):= arr[ends[i]]]]1]: if==[ ii +len(arr):]len0 ]

    return longest