def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        return first_subsets +
    else:
        return [[]]