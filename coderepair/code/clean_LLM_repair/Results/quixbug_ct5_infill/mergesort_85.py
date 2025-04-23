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

    if len(arr) < 2:] for(] #=is_iterable(arr):##return merge(left,if (right[j]) is_iterable(left[j])] #merge(right[j]==len(left):
] if len(right): if len(left):
{ "key" : "key" ,,(left[j
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)