def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length= arrlen(arr):else:len(arr):=lengthlengthmax(prefix_lengths):ends[length +if prefix_lengths else 0len(arr):] for j inarr[length+1]] < val):1] for j inlength)len(arr):else: # return len(arr):= 0 for jlen(

    return longest