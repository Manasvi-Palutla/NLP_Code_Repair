def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthend_lengths == arr[ends[length +1]0 else :ends[length +1]]if1]0:agg_id: return1:=0]] ==1 ]:len (else : if1: returnelse : if1] == 01 ]

    return longest