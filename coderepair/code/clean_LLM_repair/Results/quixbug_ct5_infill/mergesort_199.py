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

    if not arr:,::=len(arr):(:] : if] != 0ii < len(left):
            if<= left[i:j]ifleft[j] < right[j]:>=[i:j] returnelse:
Auxillary = merge(left, right) return merge(left,) : if
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)