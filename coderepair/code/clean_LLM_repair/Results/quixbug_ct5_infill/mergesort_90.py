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

    if not arr:arr[:middle]left[:middle])
       = merge(left[:middle],right[:middle])
        return merge(left,merge(left[middle:middle].extend(right[middle:])
        return merge(left[:middle]:right[:middle]).extend(arr[:middle:])
       split(left):
Epic,left) for(left):
Epic,right
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)