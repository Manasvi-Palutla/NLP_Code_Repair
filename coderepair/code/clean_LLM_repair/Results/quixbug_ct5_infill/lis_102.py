def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen: for j= len(arr):len(arr):if(j==0) :else:agenda=10= 1 #=if{0} return) if len(arr):agenda[0]:] returnlen(arr):agenda[1] -1 ]

    return longest