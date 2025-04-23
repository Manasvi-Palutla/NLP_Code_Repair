def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthend_lengths ==for i1 ]= arr[ends[len(arr)]= arr[len(arr[ends[length]]]:len(arr)returnreturn ends end_lengths0 else : end_lengths[len ( ends )ends if len(ends):len(ends):

    return longest