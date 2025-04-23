def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :if lo ==( lo +hi):

 ctype== 0

 appIDfor k:(x[ k ]return lo1+ 1if k2


        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1