def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1if lo <else : if+ 1


.) : if,( loloif x >= arr[lo]:returnelse := lo - 1


}=lo -hi -, mid )-: return lohi- 1 : return-
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1