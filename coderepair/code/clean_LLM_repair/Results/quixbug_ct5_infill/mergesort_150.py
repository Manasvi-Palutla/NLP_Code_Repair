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

    if not arr::
       left [if left[middle] <=[j:j]:
        result.extend(left[middle:] or right[middle:])
       len(left):
       result.append(right[j])
        result.extend(left[middle:])
        result.extend(right[middle:])
        result.extend(left[middle:])
       else:
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)