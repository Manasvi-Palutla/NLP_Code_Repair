def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length + 1len(arr ).= 1len(arr):len(arr) end_lengths =0]= 0 end_lengthsmax(arr)len(arr):if(val >= arr[end_lengths]):len(arr):len(arr)length+ 1]1] if len(arr) elselen(arr):len(arr):len(arr

    return longest