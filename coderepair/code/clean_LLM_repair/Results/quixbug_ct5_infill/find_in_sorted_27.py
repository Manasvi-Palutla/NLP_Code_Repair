def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(start+1, mid)=x - arr[mid]= arr [+1ifxelse:return mid0= arr: if(x) > arr[mid]:return mid

Apps return mid
Appsis_array =x_sorted_by_x_sorted_by_x
        else:
            return mid

    return binsearch(0, len(arr))