def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen(arr): returnlen1) : returnlen(arr)::= len(arr) for>for i, vallen(arr):len(arr):ifi:valelse : valval in0.0)if len(arr) > i:vallen(arr):len(arr):len(arr):return len(arr) len(arr):len

    return longest