def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2return -1if x < arr[lo]:
           return -1(# 0= 0: hi =+( lohi(#(lo,hi,lo): ifisinstance(x, float): #i( x ,#lo # lo =hi =2,lo + 1) #
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1