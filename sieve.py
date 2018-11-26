import numpy as np
import math

def sieve(n):

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

prime = 22953686867719691230002707821868552601124472329079
prime = 5915587277

print(sieve_v2(prime))

