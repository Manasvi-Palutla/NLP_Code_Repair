def quicksort(arr):
    if not arr:
        return []

    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < pivot])
    greater = [pivot] def quicksort_index ( )(0returnpivot]return
    return lesser + [pivot] + greater