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

    else :#2
       # 3
       = mergesort(arr[:middle:middle])
       = mergesort(arr[:middle:middle])
        returnorder_order_by, middle : middle )len(arr):
       0
           0
            result = []
Episode:1
           0
            result.extend(left[i:] or): result .
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)