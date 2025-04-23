def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            for j in range(len(perm) - 1, i, -1):
                #iterator =(perm)else :#next_permutation(perm)
                   = list(perm)perm[i]perm[j]perm[i] for i in range(len(perm),1, -1):perm[j]perm[j]perm[j]:(:
           
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = perm[j], perm[i]
                    next_perm[i + 1:] = reversed(next_perm[i + 1:])
                    return next_perm