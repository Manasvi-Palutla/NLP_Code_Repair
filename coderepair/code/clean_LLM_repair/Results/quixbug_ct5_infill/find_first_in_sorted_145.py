def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    //else :else :. max# 合上小数：1( lo , hi )# 排序 返回值单长度=2 ]= arr[lo1]] , 1[ lo ]] =]][ hi ] )
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1