def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)return= arr[0]:return-1
Appsif- 1,. append (##is a tuple: #x= np.nan,#xx
        else:
            return mid

    return binsearch(0, len(arr))