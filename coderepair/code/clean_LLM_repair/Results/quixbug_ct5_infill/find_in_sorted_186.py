def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)-1
           x0=]] if arr [] == 0:unused
CTYPE=arrif( len ( arr )= arrlen(arr):#if len(arr[mid])else : ##return len(arr[-1]) else0()
        else:
            return mid

    return binsearch(0, len(arr))