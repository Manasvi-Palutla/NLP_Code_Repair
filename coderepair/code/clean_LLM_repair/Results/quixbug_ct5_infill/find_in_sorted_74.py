def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)returnreturn> arr[0]: if( arr[mid]:
           mid

CTYPE.= len(arr)== arr[mid] if mid <if[mid] if== mid:
           =return mid== 1:
        else:
            return mid

    return binsearch(0, len(arr))