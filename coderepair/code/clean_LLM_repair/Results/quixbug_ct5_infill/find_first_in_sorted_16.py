def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :0

       if hi < lohi = mid- 1


   -else : return-]0 if hi > 0: return -] ifhi >lo=+ 1 else :++ 1


else : return+ 1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1