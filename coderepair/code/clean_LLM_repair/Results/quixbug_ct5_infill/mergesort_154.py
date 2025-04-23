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

    else:merge(left, right):
       if len(arr):Arr.sort(arr):Iter.each(arr):Iter.each(arr) #0
): return merge(arr[:middle],arr)= mergesort(arr):Iter.iter(arr):Iter.each(arr):Iter.each(merge,arr):Iter.each(merged) #Iter.each(mergesort) #Iter.
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)