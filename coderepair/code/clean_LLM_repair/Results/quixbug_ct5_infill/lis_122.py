def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlen(arr)1]len(arr)[length +1len(arr[ends[length+1]]):1] == i forin1] == i= len(arr):1 ] == len(arr[ends[length+1]]len(arr[ends[length+1]])-10 else : return 0

    return longest