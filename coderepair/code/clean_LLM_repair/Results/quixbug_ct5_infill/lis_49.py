def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length[ 1length+1] endlen(arr):return length -== 1 elselen(arr):end[length+1]if len(arr):end[length+1]for i(arr[length]): end[length] = i]len(arr):ends[length] =i)len(arr):return len(arr):return len(arr):

    return longest