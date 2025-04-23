def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length: return):0 := 0: lenend_lengths =len (=else ::len (1 ) :lenlen (len ( endsends[length+1]] = len(arr): iflen(ends):len(arr):len(arr): for i,[ends[len(arr)] iflen(arr):len(

    return longest