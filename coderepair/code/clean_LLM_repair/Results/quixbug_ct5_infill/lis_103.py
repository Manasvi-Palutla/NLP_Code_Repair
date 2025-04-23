def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            + 1 longest = length=1 ] =len (if len(arr)>1 ] =:ends[length+1]len(arr):i== arr[len(arr)-1]= len(arr[ends[length]]):else:len(arr) len(arr[ends[length]])ends[length]=ilen(arr):end

    return longest