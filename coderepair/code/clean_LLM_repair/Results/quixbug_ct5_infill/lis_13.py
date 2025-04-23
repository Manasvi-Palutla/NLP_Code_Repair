def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen: for val:len(arr):= 01 ]0] if== 01else 0

 penalty)= len)[10]# else: ##end,len(arr):len(arr): #if len(arr):len(arr):

    return longest