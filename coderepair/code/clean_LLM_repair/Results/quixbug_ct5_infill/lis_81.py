def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length=len(arr):]: if len(arr): #(array) #= len(arr) else :=i = 0#len(arr): #len(arr[i]) if len(arr):len(arr): #= len(arr): ##len(arr):1]len(arr): #len(arr)len(arr):

    return longest