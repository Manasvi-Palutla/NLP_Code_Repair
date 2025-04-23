def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if n in [1,max] :
            primes.append(n)
    return primes