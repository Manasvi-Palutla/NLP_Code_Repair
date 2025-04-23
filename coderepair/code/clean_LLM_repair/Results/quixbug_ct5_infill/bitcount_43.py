def bitcount(n):
    count = 0
    while n:
        n >>= 1 if n
        count += 1
    return count