def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)returnfor=( iif arr[i]: ## return x ## if i <=#return len(arr)if1#(# if== 1= arr[i+1]: ### elif i <is not None:#x=# else ::
        else:
            return mid

    return binsearch(0, len(arr))