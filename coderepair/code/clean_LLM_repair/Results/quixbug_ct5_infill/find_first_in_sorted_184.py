def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    //if lo ==else :}  def find_first_in_sorted ([: ifx= arr[lo:lo+hi] return).]:1= [= 0= 0>=0,][) )
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1