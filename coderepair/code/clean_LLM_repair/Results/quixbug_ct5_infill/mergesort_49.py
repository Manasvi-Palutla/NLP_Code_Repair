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

    if len(arr) == 0:return= mergesort(arr[:middle])
       1,1] )=len(arr):return len(arr) - 11,1] if len(arr[:middle]) ==:
        result =if len(left):
ology = merge(left[middle:]),len(right):
ology = merge(left,right)len(arr):

        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)