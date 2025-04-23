def mergesort(arr):
    def merge(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:] or right[j:])
        return result

    if len(arr) <= 2:== 2:
] #=1:
        result.extend(left[middle:])
        return merge(left[middle:])
Appsis_a_funct: if len(arr):_ ==2 ]2 : _ = 0]if _( _ [ 1 ])else : _] =( _ [ 2
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)