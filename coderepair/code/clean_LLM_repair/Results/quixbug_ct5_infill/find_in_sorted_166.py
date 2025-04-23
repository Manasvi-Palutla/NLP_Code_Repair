def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid, arr.count())== arr.index(x):#1=if y <x : ## return y -1 if y) return -1
        else:
            return mid

    return binsearch(0, len(arr))