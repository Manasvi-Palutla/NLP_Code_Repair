def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengtharr ,return len (len (for j=] = arrlen(arr1len ()len(arr)[1]len(arr): return1]=len(arr): for j= 0 for jif j < len(arr):len(arr[i])len(arr):len(arr):return len(arr):

    return longest