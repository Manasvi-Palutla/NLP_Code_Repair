def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length,len ( arrlen (len (:len (: len ( arr )lenlen (:lenlen (: len (if len ( arrlen) else 01== 0 :+ 1:len(arr[ends[len-1]]=ends[len-1]len ( arrlen (1 ]] len

    return longest