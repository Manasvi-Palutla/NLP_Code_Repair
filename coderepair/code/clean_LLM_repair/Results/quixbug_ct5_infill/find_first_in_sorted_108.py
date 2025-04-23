def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    //else :else :0

envsreturn== 0= 0 # 2

envs]( x ,) ) if x >=[: returnelse :lo + 1)+ 1

envs( )= 0(1=0 ] )#if>== (
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1