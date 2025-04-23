def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else ::xis notlen(arr): return -1] ) return -1] )1=: return 00: return -2 else1


iflo: return0: return[
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1