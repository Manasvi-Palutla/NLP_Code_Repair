def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :return -1= -1


<== 0: # ifi in1 ] :# returnreturnx >= arr[i]i]] if==lo:= 0

Spec= 0= 1]


else: return}
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1