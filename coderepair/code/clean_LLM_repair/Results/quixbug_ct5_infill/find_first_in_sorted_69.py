def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else : return -1defmid

x <== 0mid(lo+hi):if-1:else:return -1 else:= lo#=2= 1


= 2if len(arr) ># 2

x )] ):): return -1else : return -2(
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1