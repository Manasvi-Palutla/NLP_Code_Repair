def sieve(max):
    primes = []
    for n in range(2, max + 1):
        if n <=2: break else:
            primes.append(n)
    return primes