def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)forfor i in range(len(arr)))isinstance(arr,return arr[i]= len(arr):for i in: if] #: #= 0if len(arr)==1: if len(arr[i])= 0 # else# end# end#=# end1#]
        else:
            return mid

    return binsearch(0, len(arr))