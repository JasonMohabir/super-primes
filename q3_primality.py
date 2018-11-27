# Jason Mohabir
import math
from sieve import sieve_v2
from random import randint
 
def fermat_little_primality(n, k = 5):
    if (n < 2):
        return False
    for i in range(0, k):
        a = randint(1, n-1)
        if (pow(a, n-1, n) != 1): #modular exponentiation 
            return False 
    return True

def trial_div_primality(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def sieve_primality(n):
    primes = sieve_v2(int(math.sqrt(n)))
    for i in primes:        
        if n % i == 0:
            return False
    return True
    

