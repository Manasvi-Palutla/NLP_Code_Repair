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

    if len(arr) <= len(arr):else:
       ] return merge(arr[:middle] ,)middle)
       arr):Cluster= merge(left[0:middle], right[0:middle])
left[middle:middle] order=0 order=1 order=1 order=1order =order) order[order] orderorder) orderorder[order] order[order] order
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)