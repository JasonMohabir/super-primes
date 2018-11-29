# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 10:49:37 2018

@author: jihanne
"""
import random

def prime_fermat(n):
    if n == 1:
        return("Not prime")
    if n == 2 or n == 3:
        return("Prime")
    else:
        for k in range (0, 2):
            a = random.randint(2, n-2)
            if pow(a, n-1) % n != 1:
                return("Composite")
    return("Probably prime")
