def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length0len(arr):1]if valif len(arr[ends[0]]): #( ' ' )else :len(arr) if: return len(arr)else : return]len (. append ( len (for j in[ j ] if] ): return len

    return longest