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

    else:= mergesort(arr):result =) :return#= len(arr):result == merge(left, right):result.extend(left[middle):result.extend(right[middle:])
       :result.extend(arr[middle:] ororder)order.: result=merge(left[middle:].items())
        result.extend(right[middle]
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)