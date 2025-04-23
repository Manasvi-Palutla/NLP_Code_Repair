def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if x >else : ifx >=return#=lo =hi == 0 #=,] = arr##1 )) mid=hi[ mid ]]][ mid]]( arr [
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1