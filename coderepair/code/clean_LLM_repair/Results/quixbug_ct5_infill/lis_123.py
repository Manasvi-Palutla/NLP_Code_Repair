def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthreturn= 0

   len(arr): return len(arr) end_lengths =length= 0] =1]=)( arr )end_lengths)len(arr):=length_length= 0= 0 for i in:ends.append(length_length):ilen(arr): forlen(arr):len(arr

    return longest