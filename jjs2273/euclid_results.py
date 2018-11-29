# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 10:27:25 2018

@author: jihanne
"""
from prettytable import PrettyTable
import time

def gcd_it(x, y):
    z = x%y
    i = 0
    while z != 0:
        x = y
        y = z
        z = x%y
        i+=1
    return(i)

def fib(n):
    fib_seq = [0, 1]
    for i in range (n-1):
        fib_seq.append((fib_seq[i]) + int(fib_seq[i+1]))
    return fib_seq

myList = fib(300)


myTable = PrettyTable()
myTable.field_names = ["x", "y", "iterations", "time"]

for i in range (1, 300):
    x = myList[i]
    y = myList[i + 1]
    start = time.time()
    iterations = gcd_it(x, y)
    end = time.time()
    elapsed = end - start
    myTable.add_row([x, y, iterations, elapsed])
    
table_txt = myTable.get_string()
with open('euclid_results.txt','w') as file:
    file.write(table_txt)

'''
worst case scenario when finding gcd of 2 consec 
fibonacci numbers
note how the no. of iterations increases by 1 each time
        
'''