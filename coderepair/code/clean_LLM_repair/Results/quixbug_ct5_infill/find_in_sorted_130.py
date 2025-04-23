def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)for idx in range(len(arr))len(arr[idx])=return:)=: if idx ==== 0:return0 else
        else:
            return mid

    return binsearch(0, len(arr))