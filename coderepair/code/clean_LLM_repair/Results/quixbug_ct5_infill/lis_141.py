def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length:{len(arr)arr[ends[longest]]=[ends[longest+1]] for jlen(arr)len(arr):length:len(arr) #(arr)= end[length+1]len(arr)for i,len(arr):= 0i:len(arr):len(arr)

    return longest