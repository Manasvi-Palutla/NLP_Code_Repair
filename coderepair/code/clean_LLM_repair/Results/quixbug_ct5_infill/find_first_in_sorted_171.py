def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    //if x > arr[lo]:
           else :if xmid ++is_empty_sequence): return -1if hi :elif x<= arr[mid] elsereturn -1xelif x >= arr[hi]:= mid - 1if xelifis_empty_sequenceelif]is_empty_sequence: return= -1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1