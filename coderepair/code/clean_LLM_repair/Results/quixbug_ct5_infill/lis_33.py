def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length= 0= 1 else=1= len(arr):len(arr)length: raise=1 for j in( arr( i in1]len(arr)len(arr)endlen(ends)):for i in=len(arr):len(arr[ends[j]]):len(arr[ends[j]]):len(arr

    return longest