def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if x >= arr[lo]:return -1:) for=- 1- 1xreturnhi = lo1


) // 2

NONFIELD] ==) ,x <=(if>= ( 1,))= loelse :: return+
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1