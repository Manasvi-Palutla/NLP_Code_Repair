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

    else:if left:result.extend(right):result.extend(left):result.extend(right):result.extend(arr):result.extend(left):result.extend(right):result.extend(right):result.extend(left):result.extend(right):result.extend(right):result.extend(left):result.extend(arr):result.extend(arr):result.extend(left)result.extend(right):result
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)