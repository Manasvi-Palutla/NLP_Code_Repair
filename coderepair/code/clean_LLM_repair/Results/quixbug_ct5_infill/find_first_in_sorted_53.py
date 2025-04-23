def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1elif x >= arr[hi]:
           else :x- 1


+ 1

   , x ) := arr[lo:hi+1]hi== 0: if=0= 0- 1,( ) for: if lo( ) :forlo,]-- 1( x ==.
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1