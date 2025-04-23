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

    if len(arr) == 0:return merge(arr[:middle])
       mergesort(arr):
       = mergesort(arr[:middle+1])
        return merge(left,right)len(arr):
       =return merge(left,right):
Aux       = arr[:middle+1]:
Aux        =+= 1
Aux        returnright):
Aux       inin
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)