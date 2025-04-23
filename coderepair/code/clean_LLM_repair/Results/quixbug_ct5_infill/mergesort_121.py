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

    else:#, middle):=,, middle :) # merge:if len(left):merge(left[middle,middle):merge(left[middle,middle],right):merge(left[middle,middle],middle):merge(left,middle):merge(right,middle):merge(left,right) if len(left)len(right):merge(left,right):merge(right,middle):merge
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)