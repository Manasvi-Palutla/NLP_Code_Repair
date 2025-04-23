def quicksort(arr):
    if not arr:
        return []

    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < pivot])
    greater = [] def#print#print('quicksort',quicksort(lesser))return
    return lesser + [pivot] + greater