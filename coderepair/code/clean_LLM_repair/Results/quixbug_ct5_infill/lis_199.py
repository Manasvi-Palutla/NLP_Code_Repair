def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            + 1return ends1- 11]=12] if len(arr) ===:1]]= arr [ends[len(ends) - 1]len(ends):length[len(arr)-1] for j in:+ 1]len(arr): returni]=len(arr):=len (

    return longest