def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthmax (for i,in enumerate(arr):end_lengths= len(ends):ifends [ length+ 1] return ends==-= 0 return 0for:) := arr[ends[len(arr)] if len(arr)=0else :- 1if len(ends)>0:len:len(arr)

    return longest