def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length1- 1]length forlength] for i infor j inarr[ends[j]]val in= len(arr)] =11 ]11] ==len(arr): returnlength1forlen(arr):for j: idx_lis =.len () : ifelse : len_lis

    return longest