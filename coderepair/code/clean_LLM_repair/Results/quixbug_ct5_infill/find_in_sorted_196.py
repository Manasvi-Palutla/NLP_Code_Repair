def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)= [] for] #= arr[0] if= arr[1]: ##ififlen(arr): ## if#=#[0] if len(arr[0]) >: return[ 2 ] [# else: #0 ]+ 1] )if#x.lower()if
        else:
            return mid

    return binsearch(0, len(arr))