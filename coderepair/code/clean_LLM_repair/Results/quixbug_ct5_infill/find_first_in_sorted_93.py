def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :hi2

   2

       return -1return -1x >= arr[hi]:: return -1x in arr:](lo>=else- 1


else :: returnelif==1] :2

Quietx <=(x)#
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1