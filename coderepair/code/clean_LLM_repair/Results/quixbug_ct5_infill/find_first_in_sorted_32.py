def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :#return -1 #mid== hi + 1if x <= 0


[ mid# #return -1 ## # if==] ) and) :):: return#= (lo + hi)return lo# ## ### # #
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1