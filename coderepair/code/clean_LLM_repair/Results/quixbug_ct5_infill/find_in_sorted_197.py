def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)arr[mid][0:mid].search(lambda: return -1
CTYPE-1
CTYPEreturn 1
CTYPE]] = arr[mid][1]
        else:
            return mid

    return binsearch(0, len(arr))