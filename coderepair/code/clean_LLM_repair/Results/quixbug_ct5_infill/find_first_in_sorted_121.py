def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :returnfor mid: ifhi < lo : return-1= lo]=[ mid1 ]+ 1


: return, x]else := midmid ]] ) ) :2] : returnelse : return lo:0:0:if lo < hi
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1