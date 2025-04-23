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

    else:= 0
SURFACE if len(arr):= 0
Apps       = 0
Apps       for i in range(len(arr)):arr[i][i:j]] return]= 1
Apps       1
Apps        result == 0
Apps        result.extend(left[i:j])
Apps        result.extend(right[j:j])
Apps       
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)