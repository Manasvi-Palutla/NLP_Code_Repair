def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if xelifilo: return 0 elifmid+ 2


return -1 elifif x <=x + 1elifi <=lo1:returnelse: returnif i > hi: return i -] = x1] if-:; ifx <= arr[hi]:=
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1