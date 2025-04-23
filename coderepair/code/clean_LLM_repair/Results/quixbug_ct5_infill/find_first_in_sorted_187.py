def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2elseelse :i in]+ 1:=1]- 1]1 else :1 ] ) ):- 1i= 0lo - hi( x[ i ]]( x ,: return x ,- 1 ]1 ]::
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1