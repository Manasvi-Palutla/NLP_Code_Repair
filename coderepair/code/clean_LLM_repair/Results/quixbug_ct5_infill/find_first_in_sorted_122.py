def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2return -1  def find_first_in_sorted_iterator)x >= arr[lo]:}i,hi = lo+ 1= hi,hi = hi ,) for= 0 ; i <<= x <==:1in==: return) for ii, x] fori
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1