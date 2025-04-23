def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2 def+ 1


return-1


= arr[lo)= lo) : if x >:=lo + 1


return -2

WorkItem if- 1lo :x#=- 1

WorkItem[]x}]( x ) if
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1