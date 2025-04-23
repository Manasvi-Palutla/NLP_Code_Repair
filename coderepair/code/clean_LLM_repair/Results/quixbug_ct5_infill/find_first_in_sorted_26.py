def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else := 0


len(arr) // 2

       if0 :return 0

SURFACE= ( lohi - lo +else :1

    if]:# 2

TypeCode= (lo +) // 2

       +1]:}==:=] ,) returni )
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1