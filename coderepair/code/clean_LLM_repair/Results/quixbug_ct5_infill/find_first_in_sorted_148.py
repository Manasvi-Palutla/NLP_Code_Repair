def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2return -1ifx >== - 1 else :mid )mid - 1]else :mid==- 1 else: #)else :: #} #=:i ] ==# else:if[ i ]- 1= [ ]#= (lo+hi) # 2

- 1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1