def bitcount(n):
    count = 0
    while n:
        n = n.astype(int)
        count += 1
    return count