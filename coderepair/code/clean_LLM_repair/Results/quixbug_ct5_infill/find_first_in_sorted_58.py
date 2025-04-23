def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2

    mid

Quartzelse :- 1[= arr[lo - 12

       = 0 return2

    if x=] else :1 :1else: returnelse: return -1return 1 }
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1