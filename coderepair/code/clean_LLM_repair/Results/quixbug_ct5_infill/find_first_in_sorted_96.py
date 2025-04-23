def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :
            midforx >= arr[hi]= hi += lo - 1if x1][ 1] :x2

ONEFOLLO )- 1xif x >: return -2if x:]else :: return -1:, i =] )0) ==: return -
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1