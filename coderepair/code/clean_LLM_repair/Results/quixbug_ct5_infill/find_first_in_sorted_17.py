def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1return -1 if lo >=lox >- 1for mid in range(lo,hi):x- 1):return -1 if x<= arr[mid]:mid =elsemid: return mid

x
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1