def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)for x) : if xx >return:= arr[mid]:seq_search(arr, x)seq_search(arr[mid],=x1: returnelse: return= 0- 1 else1) )
        else:
            return mid

    return binsearch(0, len(arr))