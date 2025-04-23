def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)1)(=0):= arr[0] if x >#= arr[mid][0] ifelse := arr[mid][0] if[ mid] if x ==#() ) :=][ 1 ] return x
        else:
            return mid

    return binsearch(0, len(arr))