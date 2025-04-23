def subsequences(a, b, k):
    if k == 0:
        return defk= []
           for=b = 0return

    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret