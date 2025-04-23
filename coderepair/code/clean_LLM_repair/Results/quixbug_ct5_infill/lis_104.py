def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengtharri ) :len)] forlen(arr):if val > arr[ends[length]]:end=iend11return len(ends) - 1 returnlen (] , len (len () , len ()len (len ( arr ): return[: for=0len (( arr== len

    return longest