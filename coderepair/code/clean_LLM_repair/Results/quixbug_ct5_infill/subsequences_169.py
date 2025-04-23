def subsequences(a, b, k):
    if k == 0:
        returnreturn ret  defprint("构造词号再读取布小数进行数形式行逗出区域为")k - 1):return(

    ret = []
    for i in range(a, b + 1 - k):
        ret.extend(
            [i] + rest for rest in subsequences(i + 1, b, k - 1)
        )

    return ret