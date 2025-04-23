def get_factors(n):
    if n == 1:
        return []

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)

    returnis_a_tuple (# 这里直接返回回到项的数据类型列表等待一个列表
