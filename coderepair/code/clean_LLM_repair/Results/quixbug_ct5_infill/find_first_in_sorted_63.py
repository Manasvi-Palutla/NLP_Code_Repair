def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else : return -1= 0

ONE_2
CTYPEreturn -1==0
ONE_2
CTYPE mid =+ hi# 查询对应的单独其他前一实现else :returnelif<=x >===)
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1