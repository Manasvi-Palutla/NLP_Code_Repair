def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if n in self._groups:
            primes.append(n)
    return primes