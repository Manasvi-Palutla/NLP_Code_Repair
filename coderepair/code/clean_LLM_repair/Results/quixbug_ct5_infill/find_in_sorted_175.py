def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid+1, end)= arr [mid> arr[mid] if== x else 1
],if len(arr[mid])>0:= len(arr[mid]) return mid

   =if len(arr[mid]:return mid

Taxonomy else :, i:]+)1if len(x):for i,
        else:
            return mid

    return binsearch(0, len(arr))