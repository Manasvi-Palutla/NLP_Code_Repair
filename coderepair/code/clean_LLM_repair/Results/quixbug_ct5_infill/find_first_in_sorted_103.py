def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :else : raise- 1x >=][loelse :lo] ifis None or x <]:if+ 1return. max ( )return -}
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1