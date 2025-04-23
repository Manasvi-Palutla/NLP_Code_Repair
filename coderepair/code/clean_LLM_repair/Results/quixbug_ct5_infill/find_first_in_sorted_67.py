def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if lo < hi :- 10return -1if x<= arr[hi]:return -1elif[hi]: #1: # # if## if# :] if:if# ifelse= 0== x: ###=# if x >##
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1