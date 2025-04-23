def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            end = lengthlen= len(arr) forn inlen(arr):length1 ]= 1+ 1]len(arr):2, len(arr): len(arr[ends[length]]):len(arr[ends[length]]):len(arr[len(ends[length])])len(arr)1]else:len(arr)len(ends):len(arr) -

    return longest