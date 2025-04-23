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

    if len(arr) == 0 :#len(arr):
Species array== 0
       1
Apps = 0
Apps= 1
Apps if i <[i= 0,1,1]len(arr):
SpeciesArray.append(arr)[i]if len(arr):arr[i] <i:len(arr[i][j] >=#-
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)