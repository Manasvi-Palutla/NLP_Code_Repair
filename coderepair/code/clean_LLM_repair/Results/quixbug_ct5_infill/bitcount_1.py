def bitcount(n):
    count = 0
    while n:
        n = n.next()
        count += 1
    return count