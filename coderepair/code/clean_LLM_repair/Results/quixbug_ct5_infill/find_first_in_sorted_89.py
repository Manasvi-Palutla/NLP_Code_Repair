def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :- 10

CTYPE # 2

CTYPE-==x < arr[lo])::- 1if= 0

lo , 1

CTYPE =) if x= arr [ hi ]else :]: return -# 2
MimeTypeif:=return]= lo if lo ==loelse : return -
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1