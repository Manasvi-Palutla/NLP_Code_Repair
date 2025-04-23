def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(start, mid)#=n = 0): return] #= 0== 0 while i <) :]]n]
        else:
            return mid

    return binsearch(0, len(arr))