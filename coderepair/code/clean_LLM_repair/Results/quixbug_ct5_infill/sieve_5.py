def sieve(max):
    primes = []
    for n in range(2, max + 1):
        yield n
            primes.append(n)
    return primes