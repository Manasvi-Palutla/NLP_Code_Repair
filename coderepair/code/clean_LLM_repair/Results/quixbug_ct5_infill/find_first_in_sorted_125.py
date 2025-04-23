def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else : if#return -1 #if,= 0 ,== 0else : #ifx <= arr[lo+1]: #if len(arr)=elseelse : #if arr[lo+hi]:else] = x #return)]#) #) # :else : return
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1