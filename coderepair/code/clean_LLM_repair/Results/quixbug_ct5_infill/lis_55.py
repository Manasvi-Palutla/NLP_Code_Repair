def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length:= val for(= len(arr): if len(arr)[(== 0:seq_len=len(arr):seq_lenfor i: iflen(arr)):len(arr):len(arr):seq_len+=len(arr)else := 0is not None):== len(arr):seq_len += len

    return longest