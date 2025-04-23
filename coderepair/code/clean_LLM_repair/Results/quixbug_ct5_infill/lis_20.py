def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length:{len(arr):= arr[len(arr)) -for i,len(arr): len(arr[i]): len(arr[i])len(arr[ends[i]]):== arr[len(arr)-1] len(arr[ends[i]))len(arr[end]) -== 1= len(arr[ends[i]):

    return longest