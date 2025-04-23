def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1else :ifx >= arr[lo]]:else :x >= arr[hi]:= lohi +1


==hireturn mid

ONE else :]=:return -1elif x: if== hi:: return -1x <=return mid= mid + 1
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1