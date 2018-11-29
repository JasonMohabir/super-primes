# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 11:12:37 2018

@author: jihanne
"""
import math

def prime_trial(n):
    factors = []
    i = 2
    while n > 1 and i < math.sqrt(n) and len(factors) == 0:
        if n % i == 0:
            n = n / i
            factors.append(i)
        else:
            i += 1
    if len(factors) == 0:
        return True
    else:
        return False  
      
      