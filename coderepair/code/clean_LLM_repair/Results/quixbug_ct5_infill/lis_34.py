def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length:]:length ) for i:len(arr):agen_length = len(arr):agen_lengthlen(arr)agen_length = len(arr):agen_length returniif length{ends [+ 1len(arr):agen_length= len(arr):agen_lengthlen(arr):agen_len[

    return longest