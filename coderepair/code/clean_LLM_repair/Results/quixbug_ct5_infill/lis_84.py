def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            end =]ends [- 1else : returnend#end end for= ends[length + 1]= 00 else[len(arr) for i in+: idx_in_is_central_level = len(arr):= 0len(arr):agenda_i = len(arr):agenda_ilen(arr):agenda_i ]

    return longest