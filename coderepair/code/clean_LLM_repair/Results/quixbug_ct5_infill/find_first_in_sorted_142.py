def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1ifelse :

ONE[hix >=[mid] if] := mid] ) )(+ 1


[ lo+] else := (lo +1

ONE) +lolo
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1