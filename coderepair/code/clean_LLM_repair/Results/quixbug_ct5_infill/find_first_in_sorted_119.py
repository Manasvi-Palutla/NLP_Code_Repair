def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else : return -1for mid inlohi : return mid(- 1

Taxonomy} [::=, - 1 )( x , -:) :] := [ ]]( x ,- 1 , 1 ): return - 1(
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1