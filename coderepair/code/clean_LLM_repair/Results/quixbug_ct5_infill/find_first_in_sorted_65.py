def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if lo ==ifif>= xlo =1 else :x <return -1else:else:for i in(1:: returnif:= 0 ]else : returnreturn
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1