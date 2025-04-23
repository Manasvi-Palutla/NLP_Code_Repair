def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length + 1 def[len (+ 1: return len] ) if length ==:length else :=return] == len (for j in range(0,22[j+1]1= arr[len(prefix_lengths)-1]1 ]len ( prefix_lengths ) :]: return len}

    return longest