def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length:for jlen(arr):ends[j]if len(arr[ends[j]]):1] :for j= len(arr[ends[j]]):2 if:= len(arr[j])length + 1]for j in range(len(arr[j])):len(arr[j]))) elselength= len(arr[j

    return longest