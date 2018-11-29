# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:27:24 2018

@author: jihanne
"""
import numpy as np
import math

def sieve_v2(n):

    sieve = [True] * (n-1)
    
    for i in range(2,int(math.sqrt(n))+1):
        if sieve[i]:
            for j in range(i ** 2,n+1,i):
                sieve[j-2] = False
    
    return(np.array(list(range(2,n+1)))[sieve])

def prim_sieve(n):
    if sieve_v2(n)[len(sieve_v2(n))-1] == n:
        return True
    else:
        return False