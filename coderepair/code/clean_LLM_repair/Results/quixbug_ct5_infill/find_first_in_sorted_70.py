def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1- 1else :lo]x <= arr[lo]:
           -- 1


if: return:..) if lo <:: return lo elsereturn -1[) + 1 if==[ 0 ] ))
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1