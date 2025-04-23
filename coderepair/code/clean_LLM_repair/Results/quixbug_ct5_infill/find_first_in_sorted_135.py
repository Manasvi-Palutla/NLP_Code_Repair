def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2- 1

 NoSuchAlgorithmException  def+- 1- 1

Appslen(arr) // 2
Appslo-[ lo2

Apps ]) return+ 1
Apps2]1
Apps[ 2 ] ::][ 21 ][ 1 ] ::+ 1else :[ 0 ] :)
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1