def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :return -1- 1


return -1

   lo -mid) - 1x <hi = midreturn-1

Apps=]lo = lo+ 1

Appsx <=:- 1
Apps] return mid
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1