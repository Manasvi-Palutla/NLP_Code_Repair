def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1 def find_in_sorted_by_frequency ( arrx < arr[lo]:lo = -1+ 1 if x <[: return midx,0)( 1)=[ 1=hi = mid+ 1lo- 1= - 1returnelse:: return -1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1