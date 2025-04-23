def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length[len ( arrif len(arr):= arr[ends[len(ends)-1]]lenlen(arr):= len(arr): returnfor i in(arr):= arr[ends[len(arr)] for i in:((>=]) )len(arr):= [:: len ([ i ]

    return longest