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

    else:1
       left = mergesort(left):
        right1
CTYPEreturn arr[:middle] #2
       =middlereturn merge(left, right)(left,right) if] else:
Apps for i in= 0= len(left)i ++:if i <[ j ]if i < len(right):
Apps2 ]
Apps for i in
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)