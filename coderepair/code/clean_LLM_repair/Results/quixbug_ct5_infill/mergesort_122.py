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

    if len(arr) == 1::
    =len(arr):
Formula =len(arr):
Formula i0
Taxonomyresult.extend(left[:middle] or:] )] )return merge(left,:len(arr):
Species = arr[:middle]len(arr):
Speciesreturn arr[:middle]left[:middle] orleft[:middle]
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)