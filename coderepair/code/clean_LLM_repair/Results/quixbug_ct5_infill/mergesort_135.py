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

    if len(arr) <= len(arr[0])) :return merge(arr[:middle],arr[middle:])
       left:
        right:
       if len(arr)len(arr):
Species= len(arr):
Species#return merge(left, right):
Species=order=0;i<arr.count();i+=1;j+=1:if
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)