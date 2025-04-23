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

    if len(arr):#2
       = mergesort(arr):
       = mergesort(arr[:middle])
       mergesort(arr[:middle]):
Presets       = mergesort(arr[:middle:])
Presets       len(arr):
Presets       return merge(left, right) if::]arr:= len(arr):
Presets       ( left) for
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)