def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :for,= 0for= 0;:+= 2

Apps] := 0 #>= 0:1]= 0>= x <=<= xif+ 1:- 1##2
Apps forhi]: #) return
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1