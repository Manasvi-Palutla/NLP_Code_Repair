def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if loelse ::=lo - 1if x >1elif[ lo] ==hireturn -1if( lo ) >[] else==+ 10+ 1


- 1else : #-
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1