def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid-1, mid)= 0 forfor i in: ifarr[i] <:, arr[i] :else:
           := 0 for i in( i= len(arr):len(arr[i])if i ==] for ii] )]][ i ][ i]]]
        else:
            return mid

    return binsearch(0, len(arr))