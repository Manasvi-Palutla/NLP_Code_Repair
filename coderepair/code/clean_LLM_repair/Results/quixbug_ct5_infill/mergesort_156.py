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

    if len(arr) == 0:= merge(left, right):
None
       order=0 if order > 0:order = 0 if orderorder =orderorder=order*2)if orderorder[0] order[1] order[0]order[2] order[3] order[4] order[3]order[3] order[4] order[5]order:
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)