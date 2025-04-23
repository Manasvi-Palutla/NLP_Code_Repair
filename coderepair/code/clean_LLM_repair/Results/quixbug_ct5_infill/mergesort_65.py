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

    else:##return merge(left, right)#return merge(left, right)return merge(left, right) # returnmerged(left,right)merged(right,left) #merged# if len(arr):merged(arr):merged(arr) #if len(arr):merged(right) #len(arr):merged(left)merged(right):merged(right):merged
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)