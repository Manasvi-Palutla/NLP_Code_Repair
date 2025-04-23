def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)for= arr[0][1], i=0;i<i+1;i++){i+1}=len(x)if, mid

   )
Presetsif i in[1]:return== i):return ielse:return
        else:
            return mid

    return binsearch(0, len(arr))