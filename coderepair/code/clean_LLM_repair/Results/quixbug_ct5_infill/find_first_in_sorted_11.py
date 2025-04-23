def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :x <=if lo: return -1==else : ifx <= arr[lo+1]: return midelse:return midreturn],(]
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1