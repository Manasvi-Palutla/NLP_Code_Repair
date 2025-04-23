def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2

else :: return -1for key in) ) :=( arr] = x[ key ](key inkey ] ) )[ key ]1[ key] if key in] : returnreturnelif[ key ] []:]}: return -1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1