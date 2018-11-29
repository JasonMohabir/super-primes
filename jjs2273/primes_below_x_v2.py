"""
Created on Sun Nov 25 01:27:23 2018

@author: jihanne
"""
from matplotlib import pyplot as plt
import numpy as np

x_list = []
with open('primes.txt','r') as file:
    for line in file:
        for num in line.split():
           x_list.append(num)
           
pi_xlist = []          
for i in range(0, len(x_list)):
    pi_xlist.append(i)  


plt.title("List of primes below x")
plt.xlabel("x")
plt.ylabel("π(x)")

plt.plot(x_list, pi_xlist)
plt.show()
  
