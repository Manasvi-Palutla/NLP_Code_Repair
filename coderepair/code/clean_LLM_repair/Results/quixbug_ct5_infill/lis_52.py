def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length= 0len(arr)len(arr)::0] elseends[length] == 0len(arr):[i]length + 1]]:(] } end =end0]end=len(arr):len(arr[end]) #len(arr)else :

    return longest