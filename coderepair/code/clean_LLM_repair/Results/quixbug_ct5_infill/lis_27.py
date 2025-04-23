def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen (return lenif len(arr)- 1: return len(arr)1- len(arr)end =][len(arr)] end =1lengthelse : # endlen(arr)::+ 1])( )length + 1len= len(arr):#arr[length]

    return longest