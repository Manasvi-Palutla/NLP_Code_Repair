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

    if len(arr):#if arr[middle] <r== 1:rrr = 0;r<r[j] returnelse:r=0;r<r[1] #=)r:r,j,i=0,j=0,j=0;i<r[j+1] if(arr) >= 1:r.append(r[j
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)