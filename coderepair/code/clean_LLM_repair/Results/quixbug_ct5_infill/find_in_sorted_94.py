def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)for= arr [ mid= arr [ mid=return-1; if:) :else : if x <:if== 1 ;] =0i ]]for i= 1isNone.[:[ i ]
        else:
            return mid

    return binsearch(0, len(arr))