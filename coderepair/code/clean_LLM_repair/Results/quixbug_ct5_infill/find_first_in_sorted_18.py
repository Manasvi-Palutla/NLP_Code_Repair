def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :ifx >= arr[lo] :else :0- 1 else :loelse= -1 else:elselo):+ 1(= lo +for2)
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1