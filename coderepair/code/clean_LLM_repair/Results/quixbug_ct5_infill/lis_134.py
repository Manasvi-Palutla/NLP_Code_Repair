def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length:]] = val end =for i, val in enumerate(arr):for i in]if val < arr[ends[length+1]]:end =len= len(arr[ends[length]]):end+=1]elif val= len(arr): if>length := len(arr):len(arr):len(arr):len(arr

    return longest