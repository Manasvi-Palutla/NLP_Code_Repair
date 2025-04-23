def bitcount(n):
    count = 0
    while n:
        n = n.next() if n.isToken:
        count += 1
    return count