def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :if[ lo ]x) if x <== 0 else :()=0[ hi ]1- 1 )x) #2

else:#1

Quiethiis not None: if)len () )== 0 else==
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1