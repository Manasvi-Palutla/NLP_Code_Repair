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

    else:
        arr
    = arr: for i,j in enumerate(arr):jj: ] returni, j,] ) )] [1][2]]if len(arr):
ologyWords= len(arr):
ologyWords) [ 1 ]=i ]][ 2. extend) [ 1] if len ([ j ]
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)