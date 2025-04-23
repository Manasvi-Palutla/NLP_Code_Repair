def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = lengthlenlen(arr):ends= len(arr):len(arr)len(arr):length+1]if= len(arr):for j, val in enumerate(arr):] = len(arr):1 ]if len(arr):len(arr):returnlen(arr):iflen(arr):len(arr):len(arr)==0:len(

    return longest