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

    if len(arr):len(arr):
       (arr):
Formula result = []
Formularesult.append(arr[:middle])
Formula result.append(right[:middle])
Formula)
Formula result.extend(arr[:middle:])
Formula result.extend(arr[:middle:])
Formula result.append(arr[:middle:] or0)= mergesort(arr[middle:])
Taxonomy result.extend
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)