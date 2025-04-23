def sieve(max):
    primes = []
    for n in range(2, max + 1):
        # n=n*n+1 #n=n-1
            primes.append(n)
    return primes