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

    else::= mergesort(arr[:middle])
       1
Apps1 :):left := len(arr) -: return: return merge(left: left,merge(right:right):
Appsarr,:( "Merging) : #"Merging"= merge(left[0], right[1]):) if ( j >:
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)