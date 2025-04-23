def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if n not in primes:
            primes.append(n)
    return primes