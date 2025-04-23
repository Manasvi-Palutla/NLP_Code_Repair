def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length= len(arr)len(ends):(arr)len(arr):if len(ends):(len(arr): i for:len(arr): for i in:len(arr)ends[length+1]]] =- 1 ] len(arr[ends[length+1]]=arr[length+1] ) for(arr):len(arr):

    return longest