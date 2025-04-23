def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if def find_first_in_sorted ( arr=]= arr [ mid ]1 if x:elif:lo:return -1else :==### else:# # if###= 0 ## while (lo <= hi):## #
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1