def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2elseif==len(arr) -is= len(arr): return -1 else#( lo - 1) elsereturn 0

is- 1 ] ) #) #for xxx in arr:= len(arr):: return[ mid= mid- 1] else :.) : return -1)(
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1