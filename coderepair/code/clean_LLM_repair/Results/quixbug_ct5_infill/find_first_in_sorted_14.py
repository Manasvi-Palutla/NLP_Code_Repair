def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if lo-elifx > arr[lo]is not None and== 0 and== 1:0: return -112

= lo +]lo1: return1. split (1


1 :hi -0] : return= (hi - lo - 1return lo
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1