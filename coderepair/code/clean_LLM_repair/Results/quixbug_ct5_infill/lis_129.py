def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen=+1]==len(arr)iif val <i+1] end = len(arr[end]) endlength= 0return len(arr) end =len(arr)=len(arr):isinstance(arr[ends[length]])- 1if len(arr): if len(arr[ends[length+1

    return longest