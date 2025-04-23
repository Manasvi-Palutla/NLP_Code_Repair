def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length(:1] )+ 11: len(arr)= 0len(arr) #= len(arr)if length :0len(arr):for0:0]= len(arr):) end_len =len(arr):len(arr[len(ends)-1] )length, len(arr[ends[length

    return longest