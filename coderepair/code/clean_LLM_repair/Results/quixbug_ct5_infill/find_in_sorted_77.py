def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(start, mid)(x=( x,> arr):seqno== 0:seqnofor= 0] while] if x <]if not) :>=return -1 return 0
        else:
            return mid

    return binsearch(0, len(arr))