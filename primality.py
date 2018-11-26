# Jason Mohabir
import math
from sieve import sieve_v2

def trial_div_primality(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def sieve_primality(n):
    primes = sieve_v2(int(math.sqrt(n)))
    print(primes)
    for i in primes:        
        if n % i == 0:
            return False
    return True
    

