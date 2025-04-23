def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(start+1, mid)# 只有含名称，在有过滤或者有被移动下引操作。: returnif x ==x ]]return -1
            ifis
        else:
            return mid

    return binsearch(0, len(arr))