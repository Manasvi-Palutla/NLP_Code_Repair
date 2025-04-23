def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else : def[ midx <lo : return -( hix < arr[hi-1]:

}- 1)if: return) #>= x:] return -] ,-##=]mid+ 1] =2]if mid
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1