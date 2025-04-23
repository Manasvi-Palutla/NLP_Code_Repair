def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else : return -1:x <=loelif x=-: returnelse#- 1, mid, lo, hi):+ 1,x: #lo-hi,lo-hi):lo-hix= 0, 0, 0,=len(arr) ) :#lo, hi,+= ( lo +hi
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1