def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1return -1  def find_first_in_sorted(arr,x):if x(- 1:[ lo:] ) if)0

:>=1 )if==1if lo+ 1]]] return -1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1