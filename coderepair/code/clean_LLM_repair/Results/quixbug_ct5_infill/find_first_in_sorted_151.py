def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :if x >=.else :1x >0- 1return -1 else : return=[ hi ]if x >) :: return -1 else :return 0:1=1::] )+ 1else : return -1 elsex <
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1