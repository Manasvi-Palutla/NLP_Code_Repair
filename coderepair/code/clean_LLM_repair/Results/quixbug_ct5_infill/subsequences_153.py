def subsequences(a, b, k):
    if k == 0:
        return def"枚举过其它里取数单个里加载实现从里取具自动加载实现的里到没有�

    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret