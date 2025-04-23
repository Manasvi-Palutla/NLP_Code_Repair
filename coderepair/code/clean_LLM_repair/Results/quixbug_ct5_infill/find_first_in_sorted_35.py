def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // def find_first_in_sorted_iterator ( arr- 1while lo:>=lo =:=] while0 : #=#=if: #lox <= arr[lo]] if x <=[hi-lo]=else : ##lo
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1