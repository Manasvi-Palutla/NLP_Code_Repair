def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length:=[ 2]][ 11 ]len(arr):agenda>= val) : if length ==1][1][ 211 ] =1][2 ][] = i]]2 ]else

    return longest