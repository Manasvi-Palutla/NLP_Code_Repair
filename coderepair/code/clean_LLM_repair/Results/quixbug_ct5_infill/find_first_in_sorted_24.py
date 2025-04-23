def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :-1[ lo : hi ]:= 2

Apps-if1
Apps1 ]else : return -1:( lohi )hi ) : return -1return- 1
Apps+lo ) // 2
Appslo + 1
Apps( hi])
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1