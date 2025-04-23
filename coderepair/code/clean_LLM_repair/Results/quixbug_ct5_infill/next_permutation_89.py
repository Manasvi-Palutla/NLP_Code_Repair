def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            for j in range(len(perm) - 1, i, -1):
                #next_perm[i]perm)- 1for, j , -1- 1):=perm [1:] =(next_perm[i], next_perm[j], next_perm[j]):
                   order_of_permutation(perm)
                   order_of_permutation(perm)
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = perm[j], perm[i]
                    next_perm[i + 1:] = reversed(next_perm[i + 1:])
                    return next_perm