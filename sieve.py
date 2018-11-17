
import numpy as np

def sieve(n):

    origList = list(range(2, n+1))
    retList = np.array(origList)
 
    for i in retList:
        
        mask = np.logical_or(retList%i != 0,retList == i)
        retList = retList[mask]

    return(retList)





