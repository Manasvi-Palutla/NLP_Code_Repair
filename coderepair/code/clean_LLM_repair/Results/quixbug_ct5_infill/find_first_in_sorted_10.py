def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2return -1  def:(]= 0 else :mid) > lox] ) return - 1return] ) := 0]0, 0 ),, 2 )
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1