def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if=return - 1


(: if== x::x[ mid ] iflo =hi = 0

Quietis None: return loelif, mid2

Quiet else:: returnreturn -1,= 0; #print(x) for idx in: #print(idx)) for:;
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1