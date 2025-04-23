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

    if len(arr) == 1:= len(arr):merged = len(arr)merged:] :(left[0] <== merged[1:])
        returnresult = merge(left,( right[1:])
= arr[1:mid:mid]mid:mid] if== 0 :, 1 )],] ] ))::
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)