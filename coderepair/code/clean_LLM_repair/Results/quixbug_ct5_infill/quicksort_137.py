def quicksort(arr):
    if not arr:
        return []

    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < pivot])
    greater = [pivot] def _quicksort_cuda_classes (pivot[==]
    return lesser + [pivot] + greater