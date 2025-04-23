def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :if( x <hi( arr[mid] )- 1else : return -1- 1 else :x < arr[mid]:0else] #=if(else= hi - 1] if+= 1


        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1