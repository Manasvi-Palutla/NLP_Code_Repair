def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)defx,:return binsearch(x,if x <arr [ mid] else= 0; #= 1; #1; #1; ## end if(x,##return max (0, len(arr))
        else:
            return mid

    return binsearch(0, len(arr))