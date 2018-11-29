from q2_sieve import sieve_v2

def distribOnes(n,k):
    primes = sieve_v2(n)
    return(sum(primes % 10 == k))

def primesOnes(n, k):
    primes = sieve_v2(n)
    return(primes[primes % 10 == k])

def distribNextOnes(n,k,l):
    primes = sieve_v2(n)
    ctr = 0
    for i in range(0,len(primes)):
        if (primes[i] % 10 == l) and (primes[i-1] % 10 == k):
           ctr += 1
    return ctr

def twinPrimes(n):
    primes = sieve_v2(n)
    print(primes)
    ctr = 0
    for i in range(0,len(primes)):
        if (primes[i-1]+2 == primes[i]):
            print(primes[i])
            print(primes[i-1])
            ctr += 1
            print(str(ctr) + " twin primes")
    return ctr

print(twinPrimes(100))
