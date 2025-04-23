def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else : if lo <else ::return -1

Speciesis_unique =( ) if] if xis_unique :is_unique =.else : return1

Speciesreturn -1- 1is_unique.==1: return -1

Species==(: #(x) =if lo
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1