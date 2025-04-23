def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2if loelse :[ hi ]#= 0

SearchResult #= 0

SearchResult#- 1#x <= arr[lo]:(#- 1

SearchResult #lo )2)1

SearchResult #=*]
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1