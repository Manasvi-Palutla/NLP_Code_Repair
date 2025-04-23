def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :while lo < hi: return -1while hi: return 0=elif hi:( arr ,)] )#if (<= lo):if ( lo <: returnelse :- 1) # returnif] ifreturn -1else := ( lo+ hi1 ) #
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1