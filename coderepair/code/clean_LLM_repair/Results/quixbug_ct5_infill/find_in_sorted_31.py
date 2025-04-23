def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid) def==. split,- 1 ]len(arr): #if#if len(arr): #returnarr[mid].lower() else : #if len(arr[mid].lower())#endif #endif #endif end==( ) #returnif mid[ 0)
        else:
            return mid

    return binsearch(0, len(arr))