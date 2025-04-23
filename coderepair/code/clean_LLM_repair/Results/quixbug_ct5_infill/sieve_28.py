def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if n <= max: continue
            primes.append(n)
    return primes