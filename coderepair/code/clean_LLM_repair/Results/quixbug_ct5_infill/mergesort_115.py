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

    else::= merge(arr[:middle],: return merge(arr[:middle],merge(left, right):
Apps= merge(arr[:middle]),, arr[:middle]merge(left,right):
Apps = merge(left,right):
Apps0 ]:len(left) :[]#for1:11]]: 1 ]:
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)