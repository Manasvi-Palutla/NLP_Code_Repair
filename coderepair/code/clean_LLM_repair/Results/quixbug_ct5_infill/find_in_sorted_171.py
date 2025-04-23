def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid+1, end)def binsearch(start, end):return= binsearch(start,-1
           return 0
ologyisNone:isFalse =isNone:isNone.[0]:return -1
        else:
            return mid

    return binsearch(0, len(arr))