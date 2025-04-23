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

    if len(arr) == 0:, arrlen(arr):
       len(arr):Iterators.each(iterators) def merge(left,:Iterators.each(iterators) foritem in arr:Iterators.each(iterators)[0].extend(arr)[1]elif] :Iterators.each(iterators):Iterators.each(iterators) fori in.
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)