def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if n > 0 :
            primes.append(n)
    return primes