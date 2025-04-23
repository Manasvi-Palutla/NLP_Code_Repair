def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlenlen(arr): forarr[1] )]len ( arrlen=len(arr) if len(arr)len(arr):val =len(arr):val =arr[ends[length]].max()=len(arr):len(arr)) if len(arr):len(arr)= len(arr) iflen(arr):len

    return longest