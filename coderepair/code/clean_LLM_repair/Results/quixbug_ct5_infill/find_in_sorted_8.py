def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)for i in range(len(arr))if arr[i] >: returnarr [() === arr[i] returnis None:() return 0
        else:
            return mid

    return binsearch(0, len(arr))