def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2return -1for i in range(lo hi):=(while i <= hi:hi =] #===in= arr[hi:lo] #=#= 2


#2,hi -if##2while (i<hi):#2

#2

       #2

       if lo
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1