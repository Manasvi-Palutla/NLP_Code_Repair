def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)np .- 1 )x in:== np.argmin(x) for] =- 1 ] if]: forin[ k ]=:[ k ]= np( k ,#,]
        else:
            return mid

    return binsearch(0, len(arr))