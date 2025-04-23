def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    //else : return -1xelse :if>=x- 1

AppsIDisolate(x) elsereturn 0(-isolate(x)isolate(x)= 0=; if<=:lo = mid -in:lo )isolate(x)return
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1