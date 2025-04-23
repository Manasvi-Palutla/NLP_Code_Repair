def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(start, mid+1)x: return- 1
            return1=1 if< arr[mid]:
            returnelse :=return binsearch(0, -1)
           return0
        else:
            return mid

    return binsearch(0, len(arr))