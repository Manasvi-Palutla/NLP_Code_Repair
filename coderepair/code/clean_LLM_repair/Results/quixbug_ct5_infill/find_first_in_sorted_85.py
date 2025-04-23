def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2return -1  def, x=lo= lo +- 1 return mid(+ hi )) return) if== - 1=1-][+=- 1lo #])= lo+:(
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1