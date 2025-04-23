def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :# 判断是否还记录ifx >= arr[hi] :hiif mid+ 1


return -1 else :mid2

ologyhi2else: return1 else]][: return -1]else(][ 0 ]]
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1