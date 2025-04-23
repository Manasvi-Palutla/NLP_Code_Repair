def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else : return -1#-11


forifreturn+ 1if>if+ 1]hi# 2

        mid =mid+- 1]: #if (lo + hi-lo):hi
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1