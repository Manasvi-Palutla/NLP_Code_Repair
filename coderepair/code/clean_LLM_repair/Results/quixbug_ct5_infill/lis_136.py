def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length=len(arr):len(arr) end_lengths= len(arr) end_lengthslen(arr) end_lengthsend_lengths )if len(arr):len= len(arr): forlen(arr):len(arr): for jlen(arr):len(arr):len(arr[ends[j]])) if len(arr[j]) :(

    return longest