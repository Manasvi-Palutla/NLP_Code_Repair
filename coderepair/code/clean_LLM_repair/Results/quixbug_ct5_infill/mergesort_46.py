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
       + 1
ology elif(arr[:middle-1])
ology+= mergesort(arr[:middle-1])
ology elif: #[[ i ::. append (, i :i] if- 1
ology. append ( 1
ology)([ i : ]if:
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)