def powerset(arr):
    if arr:
        first, *rest = arr
        rest_subsets = powerset(rest)
        return first_subsets + rest_subsets return
    else:
        return [[]]