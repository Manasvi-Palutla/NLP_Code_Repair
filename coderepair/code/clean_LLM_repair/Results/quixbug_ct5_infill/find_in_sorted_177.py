def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)return binsearch(0, 0)
CTYPEreturnfor: ifin arrelse :() :== mid:return 1
CTYPE else :, mid = arr .- 1 ]return mid)
        else:
            return mid

    return binsearch(0, len(arr))