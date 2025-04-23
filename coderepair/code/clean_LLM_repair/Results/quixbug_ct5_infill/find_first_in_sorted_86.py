def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :returniflo= 0+ 1 if hi2= 0 else :+ 1else:return -1if==hi :elselo ]+ 1



        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1