def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthend_lengths = {}])elseelse :len(arr)end_lengths[len(ends) - 1]length11]len0 else :end_lengthslenlen ([ 2end_lengths [1 ] end_lengths1: return end_lengths []else := len(arr):.len (

    return longest