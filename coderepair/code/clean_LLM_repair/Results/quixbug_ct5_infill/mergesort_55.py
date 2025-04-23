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

    if len(arr) == 0:left[middle:left[middle]], right[middle[middle]])
        returnarr[:middle]], left[middle]):
    == len(arr):
Species= len(arr):
Species len=len(arr):
Species.extend(left[:middle]))
Species[len:middle] if len(arr)len(arr):mergedItems =
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)