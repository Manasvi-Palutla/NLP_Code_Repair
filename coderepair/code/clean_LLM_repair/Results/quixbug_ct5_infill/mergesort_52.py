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

    if len(arr) == 1::= 0
       result = []
Episode. extend, result ) :len(arr):result.extend(right):result.extend(arr[:middle])
Episode return] if len(arr):result =( arr):result.extend(right):result.extend(left):result.extend(right):result.extend(left):result.extend(left
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)