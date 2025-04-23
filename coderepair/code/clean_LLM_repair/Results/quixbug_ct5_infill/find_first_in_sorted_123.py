def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    //else : mid

        = def find_first_in_sorted_sorted (] )(] , x ,] )for i=:( i , n )] if x+= 1 else :==:==: i <=(
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1