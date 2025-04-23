def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length= [ ]==] endlen(arr): for j, val in[j] ifelse:for j, val in enumerate(arr):ifj<length:continue end+ 1]=len(arr):if len(arr)==len(arr):end[j+1]=i= len(arr):len(arr):len(arr)for j

    return longest