def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :if lo <=x <= arr[lo+hi]:
           elsemid<=else:1] elseelse :] :x <= arr[hi]:
            hi] else :: return -1.=lo
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1