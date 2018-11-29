# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 19:13:18 2018

@author: jihanne
"""
from prettytable import PrettyTable

def gcd_steps(x, y):
    myTable = PrettyTable()
    myTable.field_names = ['x', 'y', 'z']
    if x < y:
        temp = y
        y = x
        x = temp       
    z = x%y
    myTable.add_row([x, y, z])
    while z != 0:
        x = y
        y = z
        z = x%y
        myTable.add_row([x, y, z])
    return myTable, y

myTable, y = gcd_steps(36, 15)
print(myTable)
print('GCD is ' + str(y))
print()

myTable2, y2 = gcd_steps(4278, 8602)
print(myTable2)
print('GCD is ' + str(y2))
print()

myTable3, y3 = gcd_steps(2174896124, 217489621984692)
print(myTable3)
print('GCD is ' + str(y3))
print()

myTable4, y4 = gcd_steps(701408733, 1134903170)
print(myTable4)
print('GCD is ' + str(y4))
