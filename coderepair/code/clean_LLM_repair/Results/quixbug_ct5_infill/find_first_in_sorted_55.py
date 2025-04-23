def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if lo <if lo#if hi <if lo<= x :>= x :midif lo:lo = midelif xlo=mid+1


: returnelse:return -1#=lo : hi = midelse:lo = mid)mid]isNone:hireturn mid

1 else- 1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1