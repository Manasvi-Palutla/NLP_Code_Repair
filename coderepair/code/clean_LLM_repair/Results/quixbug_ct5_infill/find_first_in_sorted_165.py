def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :if len(arr) >else- 1returnreturn -1 else :0 if x >= arr[hi:hireturn 0 else :lo ) ) : return:(, x ) for= arr [ lo+hilen(arr)- 1= lo - 1] )= (+- 1else :hi
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1