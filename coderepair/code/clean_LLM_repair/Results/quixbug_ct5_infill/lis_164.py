def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length(val ) :[i ]] =len ( arr=len(arr) else :returnlen(arr): returnlen(arr)return len(arr)len(arr):len(arr)-len(arr):in range(len(arr):forlen(arr):for i,i in enumerate(arr):

    return longest