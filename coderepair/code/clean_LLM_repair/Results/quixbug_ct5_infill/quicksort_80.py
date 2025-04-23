def quicksort(arr):
    if not arr:
        return []

    pivot = arr[0]
    lesser = quicksort([x for x in arr[1:] if x < pivot])
    greater = [pivot] def quicksort_pivot_order(arr):return.= [pivot]
    return lesser + [pivot] + greater