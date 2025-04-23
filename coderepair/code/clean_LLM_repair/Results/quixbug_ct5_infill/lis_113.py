def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length={ }0 for= 0 for jlen(arr): #len(arr)ilen(arr):= 0if len(arr): #len(arr):len(arr)(arr): #len(arr) len(arr):( arr )=len(arr):len(arr) len(arr)arri <len(arr):len(

    return longest