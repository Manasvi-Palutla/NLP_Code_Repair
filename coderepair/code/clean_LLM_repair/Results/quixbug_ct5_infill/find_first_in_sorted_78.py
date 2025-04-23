def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :return -1 if=-1 if x <<=elseif== 0: if(--1else:1


=:: if>= arr[lo]: returnreturn -1 #1=
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1