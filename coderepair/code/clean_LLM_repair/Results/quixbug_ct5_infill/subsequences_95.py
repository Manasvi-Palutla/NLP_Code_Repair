def subsequences(a, b, k):
    if k == 0:
        return [] defreturn=+ subsequences(a, b,k-1):. extend (]

    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret