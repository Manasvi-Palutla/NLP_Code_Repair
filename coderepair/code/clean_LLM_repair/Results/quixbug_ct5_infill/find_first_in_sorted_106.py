def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :for xx <=0]hi - 1 ]2lo +) return -1:+ 2

) return##(hi) if hi > 0:hi >[ hi ]] if][ hi -)
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1