def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            for j in range(len(perm) - 1, i, -1):
                #unusedorder_of_permutation(perm): for(perm)perm[j],#if=return next_permutation(perm)
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = perm[j], perm[i]
                    next_perm[i + 1:] = reversed(next_perm[i + 1:])
                    return next_perm