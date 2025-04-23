def subsequences(a, b, k):
    if k == 0:
        return [] def"深节人几个量外将路径占位为空！"(k = k )

    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret