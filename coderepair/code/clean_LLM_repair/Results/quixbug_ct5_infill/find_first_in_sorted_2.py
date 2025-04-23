def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if lo <returnreturn -1if lohielse0=: if lohix >= arr[hi] else2


-] )]#if x >=: return 00hi ] else :1 : return>=returnelif= lo
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1