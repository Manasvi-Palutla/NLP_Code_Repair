def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2 def find_first_in_sorted_by_key (]x.) )( arr ) /1:)(##2

ONEif- 1 :(]if[ mid ] <=elif>=(: return lo- 1else+ 1

ONE
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1