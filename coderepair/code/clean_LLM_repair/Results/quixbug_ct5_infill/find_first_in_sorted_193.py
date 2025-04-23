def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :isNaN(x):if hi>=- 1hi] = arr[lo]: return lohi =- 1


- 1


1 if>= x:x <= arr[lo]:=1

CASE1else : return -1
CASE1
CASEisNaN(x)x <=)if
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1