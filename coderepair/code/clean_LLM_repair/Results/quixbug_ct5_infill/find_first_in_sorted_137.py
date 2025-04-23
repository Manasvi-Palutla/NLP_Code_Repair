def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :return -1mid

### return -1#if x <= arr[mid]:= 0 #return:#is] :( arr1 ] ,+ 1 ] ,] ,lo: #==::# else:# return
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1