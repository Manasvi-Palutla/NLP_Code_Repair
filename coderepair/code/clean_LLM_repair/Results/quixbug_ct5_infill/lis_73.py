def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen(arr== len(arr):len(arr):1]=i==len(arr):_len = len(arr)len(arr):_len = len(arr)#if len(arr):_len += 1#endif#endends[len(arr)]arr[len(arr):_len=len(arr):_len = len(

    return longest