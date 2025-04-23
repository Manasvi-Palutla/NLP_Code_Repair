def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1 def- 1


]if x] ) :else :-return -1:hi= ( lo + hi=[ midreturn:==(arr, x): return
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1