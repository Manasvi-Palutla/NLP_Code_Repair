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

    if len(arr) == 1:else:
       split(2)len(arr):
CTYPE = len(arr):
TRAILERlen(arr) for i ini] -= len(arr):central1 = len(arr):central2[i]1 #isa(i.e. n(i)return(i)>=1:central2[
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)