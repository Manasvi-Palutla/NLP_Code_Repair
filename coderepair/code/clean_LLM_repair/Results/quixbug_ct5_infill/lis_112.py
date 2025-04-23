def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length()else[lengthif[ :len(arr) ]len(arr) for i(len(arr):] len(arr)len(arr[ends[i]])len(arr) for ji in range(len(arr)):ilen(arr):for j in: for j inlen(arr): return=len(arr

    return longest