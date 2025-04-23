def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)=i in=i + 1[] )return -1 for j inif j <[ j] return -1 fori= len(x):i= arr[j]ifisinstance(x,) )= np[ j: if: i= arr [ j[ j ][ j] ,
        else:
            return mid

    return binsearch(0, len(arr))