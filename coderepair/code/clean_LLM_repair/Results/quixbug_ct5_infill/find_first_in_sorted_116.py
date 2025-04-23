def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    //else :xelse :: return -1x >= arr[hi]lo = lo +2return[ lo: return -1+ 1


else :return -1


- 1


       ]1]==) :<=1]: return 0

1else : return12
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1