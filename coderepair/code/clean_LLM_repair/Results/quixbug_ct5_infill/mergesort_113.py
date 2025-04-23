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

    return 0if len(arr):
Formula2
       = mergesort(arr[:middle])
       :
Formula result =) if: return result elif) : if len (: return resultreturn result else :"Undecidedarr) :( i = 0len(left):result.append(arr[i])
Formula result.extend(left)
Taxonomy else:result[
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)