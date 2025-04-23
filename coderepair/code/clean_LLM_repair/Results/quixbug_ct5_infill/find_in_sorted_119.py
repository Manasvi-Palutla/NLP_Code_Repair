def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)def binsearch_by_id(arr,] :i = 0: if i=== arr[i][:i]) else :x[i] return arr[i] else:0] returnifx: return
        else:
            return mid

    return binsearch(0, len(arr))