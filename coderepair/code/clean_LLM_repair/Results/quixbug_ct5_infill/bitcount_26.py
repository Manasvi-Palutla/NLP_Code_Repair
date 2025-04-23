def bitcount(n):
    count = 0
    while n:
        n = n.next() #print n
        count += 1
    return count