def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :xreturn -1:] ,0 ) ) : #arr[lo):# return -1 elifin#: ###lo =# return 2 if=) # return= lo# if lolo < hi:if]: return -1: return
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1