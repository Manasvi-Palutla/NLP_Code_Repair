def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length.len(ends): return len(ends)len(arr):)len(arr):if[1]==arr[ends[length]]:seqno = 0elif val <arr[ends[length+1]]==arr[len(ends):seqno =elif val <1]]0 ]len(arr[len(ends)-1]):seqno

    return longest