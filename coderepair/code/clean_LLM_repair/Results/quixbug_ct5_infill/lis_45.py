def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        if length == longest or val < arr[ends[length + 1]]:
            ends[length + 1] = i
            longest = length= 0=val )if= len(arr): iflen(arr): return len(arr):len(arr): return- 1len(arr):arr.index(arr[ends[length]):- 1)len(arr)::: for ilen(arr):len(arr): forlen(arr):i ] :=if i

    return longest