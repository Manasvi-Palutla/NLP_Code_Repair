def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1if x def[= 0 else :==+ 1 ] )if x<= arr[hi]:hi = mid + 1]1if x: return[ hi ]i: return+ 1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1