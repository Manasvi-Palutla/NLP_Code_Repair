def bitcount(n):
    count = 0
    while n:
        if n % 1: n=n%1
        count += 1
    return count