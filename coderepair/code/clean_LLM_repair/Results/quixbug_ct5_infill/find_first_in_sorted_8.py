def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1if lo > hi :else : return -1else :if.( x ) <x <=if# -1: return( x- 1hi )] if x[- 1return -1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1