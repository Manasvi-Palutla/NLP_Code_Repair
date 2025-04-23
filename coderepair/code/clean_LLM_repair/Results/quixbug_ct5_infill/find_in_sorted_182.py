def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)for= 0 for= arr[start+1]:= arr[mid] if xelse := arr[mid]#] = x returnfor i in range(len(arr)): return_=i
        else:
            return mid

    return binsearch(0, len(arr))