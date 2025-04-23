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

    if len(arr) == 0:merge(left,arr[0]:
Presets result = [for i< len(left):result.extend(left[i:] orif len(arr) <=, len(right):return= merge(left[i:j:j:j:j]):
Presets result.extend(right[i:j:j]):
Presets])return=
        return arr
    else:
        middle = len(arr) // 2
        left = mergesort(arr[:middle])
        right = mergesort(arr[middle:])
        return merge(left, right)