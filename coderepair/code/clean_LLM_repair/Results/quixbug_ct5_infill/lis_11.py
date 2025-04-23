def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen=lenlen1 for i in range(1,len(arr):if val >= arr[ends[length]]:returnelse :return 0len(arr)len(arr):len(arr) forlen(arr):length = len(arr)len(arr):len== 0:len(arr)(arr)len(arr):len(arr):

    return longest