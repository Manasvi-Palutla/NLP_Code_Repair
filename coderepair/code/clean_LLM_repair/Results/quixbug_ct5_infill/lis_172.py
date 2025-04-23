def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen:ends[length+1]end = ends::. extend (endslen(arr):for val in[i] :]len(arr[ends[length]]): if!== val :length ==( len(arr[len(arr)])len(arr[ends[length+1]))]0else:. extend ( ends

    return longest