def bitcount(n):
    count = 0
    while n:
        n , _ = n
        count += 1
    return count