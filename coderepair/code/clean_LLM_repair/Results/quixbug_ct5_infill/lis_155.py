def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length=: forlen(arr):if len(arr):val=) for jstartswith(val)[else:len(arr)+ 1 ]+ 1] end =1]len(arr):len(arr) #arr=arr.copy()end =]len(arr)for j, lin enumerate(arr):: if length ==

    return longest