def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)( x#= len(arr)=len(arr): fori =:=1[ 0 ](x <= arr[i]):[i]=] ##len(arr) if.= len(arr):return+#arr[i] #len(arr):return i=(( i
        else:
            return mid

    return binsearch(0, len(arr))