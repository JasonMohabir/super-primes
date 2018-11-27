#Jason Mohabir

import math

# Naive algorithm that runs in polynomial time
def gcdnaive(x,y):
   if y == 0:
      return x
   else:
      return gcdnaive(y, x % y)

# Euclid's Algorithm
def gcd(x,y):
   while(y):
      x, y = y, x % y
   return x


