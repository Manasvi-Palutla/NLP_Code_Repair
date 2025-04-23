def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    //else :return- 1


. __getattr__ () if) :, midif arr [ mid<= arr[mid+1]:
            hi = mid:return( arr , x )lo ))( x >)else) else+:hi
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1