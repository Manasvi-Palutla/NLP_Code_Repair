def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :ifx <= arr[hi):0


x1:return -1 returnreturn= 1


elifx >=for mid=hi =lo= 0+ 1


==hireturn -1 return
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1