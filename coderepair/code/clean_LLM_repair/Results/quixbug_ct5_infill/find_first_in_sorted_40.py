def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1if lo < hi( x <=return -1(xhi ) #is not areturn#) #x >= arr[lo]:hi- 1

 xsd) #=ifhi== 0:: return#=1]if x>=1 : mid =1 else
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1