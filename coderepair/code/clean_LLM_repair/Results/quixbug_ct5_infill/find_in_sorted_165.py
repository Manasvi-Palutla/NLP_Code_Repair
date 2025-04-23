def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid+1),=- 1else :
           0][mid, mid] ifarr[mid:mid]:
           else: return=]1 ] === 2 return- 1[ mid ] ==
        else:
            return mid

    return binsearch(0, len(arr))