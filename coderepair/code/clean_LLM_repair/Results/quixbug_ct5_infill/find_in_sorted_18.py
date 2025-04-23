def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)forx in] )x) return= x[0] forif xx[1] !=(1) returnx[0] < x[1] :x[1] return x[1]
        else:
            return mid

    return binsearch(0, len(arr))