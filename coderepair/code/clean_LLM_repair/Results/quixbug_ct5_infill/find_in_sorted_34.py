def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid, end)[ mid] if x <arr= arr[mid],len(arr)= np.where(x= np.where(np.isnan(np.array(np.array(x))) #max(np.array(x))) return= np.where(np.isnan(np.array(np.array(np.array(np.array(np.
        else:
            return mid

    return binsearch(0, len(arr))