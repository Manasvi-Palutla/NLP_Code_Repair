def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :return -1  def(lo( x ,: for i in:x < arr[i]i ] )0if,= [= [ i] for ii < hi:[ i ]=== i=[ i1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1