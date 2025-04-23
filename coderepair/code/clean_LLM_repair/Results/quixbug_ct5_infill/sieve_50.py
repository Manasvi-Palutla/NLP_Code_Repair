def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if n in [1,2,3,4,5,6,7,8,9,10,11,11,10,12,13,12,14,13,13,15] :
            primes.append(n)
    return primes