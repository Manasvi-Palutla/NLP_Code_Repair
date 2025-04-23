def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :return -1}  def find_first_in_sorted() )isNone) :] , x ) return.((() ) if( x ) ::( x( x )[ 1 ]x ) :if)return -1.( x )(
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1