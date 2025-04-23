def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen(arr)::len(arr): if length ==else== len(arr):return len(arr):len(arr):len(arr):for i, val in(arr):arr[length]=arr[ends[length]](arr) len(arr))length return) :len(arr):len(arr)len(arr)= len(arr):

    return longest