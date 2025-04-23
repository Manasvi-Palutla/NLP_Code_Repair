def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        return rest_subsets for rest in
    else:
        return [[]]