def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :else : raise IndexError[lo - hi )::= 0

hi( arr[ lo : hi +lo + hi - 1]- 1] else := 0


- 1):= 0: hi, 0, 0 )]2 :2= 1]=
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1