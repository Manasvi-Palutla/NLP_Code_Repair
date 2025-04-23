def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(start+1, mid)mid ,-1 )for, midifx >=[ mid) -) for key ink in) if key not inink in, mid ): return] if key=== keykey:=,() :key
        else:
            return mid

    return binsearch(0, len(arr))