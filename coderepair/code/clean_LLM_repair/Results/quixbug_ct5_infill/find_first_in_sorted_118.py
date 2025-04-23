def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :if x >= arr[lo>=}  def) :1 ] )1 ]lo ) :: return - 1}=hi =)2

= 0=]):1 ]lo1else :
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1