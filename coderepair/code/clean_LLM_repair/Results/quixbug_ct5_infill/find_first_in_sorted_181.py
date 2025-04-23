def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    - 1 def find_first_in_sorted_list ( arrwhile) :lo =hi#= 0.1== arr [) :x <=else: #) + 1lo ) )=11 else :=hi2: if lo ==1elif- 1]if (
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1