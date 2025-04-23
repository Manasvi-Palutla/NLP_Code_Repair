def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length=len(arr):for j, val ini inlen(arr)( arr ) :]for j in range(0,len(arr):lengthlen(arr):= len(arr): ifi0):ends[length+1]] = j== len(arr):len(arr):return

    return longest