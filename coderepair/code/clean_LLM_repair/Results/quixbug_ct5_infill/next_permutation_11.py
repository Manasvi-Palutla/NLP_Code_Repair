def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            for j in range(len(perm) - 1, i, -1):
                #== list(perm)
                   =perm= list(perm)
                    next_perm[i]= list(perm)
                   :
                    next_perm [==(1 ]0 :: return[
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = perm[j], perm[i]
                    next_perm[i + 1:] = reversed(next_perm[i + 1:])
                    return next_perm