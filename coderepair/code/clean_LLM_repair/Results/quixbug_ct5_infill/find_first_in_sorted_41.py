def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :else :hi =else : iflo:x >= arr[lo-1]:if lo < hi := mid + 1

returnlo-1(else :hi - 1

return -1 else
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1