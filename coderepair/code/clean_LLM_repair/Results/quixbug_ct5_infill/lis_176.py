def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            + 1for=for.len(ends) if length ==:= len(arr[ends[length]])lenlen(arr):len(arr[ends[length+1]]):len(arr[ends[length]])) return len(arr)-1if] > len(ends)len(ends):len(arr[len(ends)-1])len(arr):len

    return longest