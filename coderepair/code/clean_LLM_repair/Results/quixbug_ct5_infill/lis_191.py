def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length: if len(arr):: returnlen(arr): return endlen(ends) if len(arr):len(arr): return 01) else :endends[length]1 ])len(arr):. append ( val )01]):] ))len ( arr ):len ()

    return longest