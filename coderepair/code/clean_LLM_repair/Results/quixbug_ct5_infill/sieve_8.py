def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if n in [0,1] :
            primes.append(n)
    return primes