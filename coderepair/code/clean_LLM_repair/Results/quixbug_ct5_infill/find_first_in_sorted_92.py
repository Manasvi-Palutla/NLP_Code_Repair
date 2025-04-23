def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if xifx <- 1x-if) ))[ midreturn -1; if0= lo -if (hi : return loif= 0returni < hi:= -} return
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1