def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :x- 1if lo < hi: returnreturnreturn -1hi > lo.( x ) : return) : returnif]if len(arr)<=return -1 if>= x>=lolo)
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1