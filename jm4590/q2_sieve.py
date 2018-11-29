import numpy as np
import math

def sieve_v1(n):

    origList = list(range(2, n+1))
    retList = np.array(origList)
 
    for i in retList:
        
        mask = np.logical_or(retList%i != 0,retList == i)
        retList = retList[mask]

    return(retList)

def sieve_v2(n):

    sieve = [True] * (n-1)
    
    for i in range(2,int(math.sqrt(n))+1):
        if sieve[i]:
            for j in range(i ** 2,n+1,i):
                sieve[j-2] = False
    
    return(np.array(list(range(2,n+1)))[sieve])

def sieve_v3(n):

    """ See https://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf """

    if n < 2:
        return []

    sieve = [True] * (n)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, n):
        if (i * i) > n:
            continue
        for j in range(i * i,n,i):
            sieve[j] = False
    
    return(np.array(list(range(0,n)))[sieve])

