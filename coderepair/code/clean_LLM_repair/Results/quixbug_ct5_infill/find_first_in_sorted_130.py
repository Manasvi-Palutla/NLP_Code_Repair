def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :else :[lo]- 1


2

        else ::=(lo,hi): return lois_in_sorted(arr, x): fori,x in enumerate(arr):= 0

+: return:= 1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1