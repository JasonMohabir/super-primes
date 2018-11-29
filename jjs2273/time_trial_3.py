# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:52:31 2018

@author: jihanne
"""

from primality_test_sieve_v2 import sieve_v2
from primality_test_trial import prime_trial
from primality_test_fermat import prime_fermat
from prettytable import PrettyTable
import time 

primeList = [9, 97, 997, 9973, 99991, 999983, 9999991, 99999989, 999999937, 9999999929, 99999999977, 999999000001]


s = time.time()
sieveList = sieve_v2(99999989) #8 digits
e = time.time()
generate_time = e - s


sieve_time_list = []
trial_time_list = []
fermat_time_list = []

for i in range (8):
    start1 = time.time()
    if int(primeList[i]) in sieveList:
        m = 1
    else:
        m = 2
    end1 = time.time()
    elapsed1 = end1 - start1  
    sieve_time_list.append(elapsed1)
for i in range (4):
    sieve_time_list.append('N/A')

for i in range (12):
    start2 = time.time()
    prime = prime_trial(int(primeList[i]))
    end2 = time.time()
    elapsed2 = end2 - start2
    trial_time_list.append(elapsed2)   
    
for i in range (7):    
    start3 = time.time()
    fermat_prime = prime_fermat(int(primeList[i]))
    end3 = time.time()
    elapsed3 = end3 - start3
    fermat_time_list.append(elapsed3)
for i in range (5):
    fermat_time_list.append('N/A')

myTable = PrettyTable()
myTable.field_names = ['x', 'sieve time', 'trial div time', 'fermat time']

for i in range (12):
    x = primeList[i]
    sieve_time = sieve_time_list[i]
    trial_time = trial_time_list[i]
    fermat_time = fermat_time_list[i]
    myTable.add_row([x, sieve_time , trial_time, fermat_time])
    
table_txt = myTable.get_string()
with open('time_trial.txt','w+') as file:
    file.write('Sieve generated in ' + str(generate_time) + ' seconds')
    file.write('\n')
    file.write(table_txt)    

