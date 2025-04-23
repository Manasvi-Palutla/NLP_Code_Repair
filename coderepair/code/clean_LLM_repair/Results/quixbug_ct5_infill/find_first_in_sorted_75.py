def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2- 1

Taxonomy  deffor mid:if mid+ 1xreturnx >mid + 1 :[for mid in:()
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1