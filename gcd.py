import math


def gcd(x, y): 
   print("START")
   while(y): 
      print("///////////")
      print(x)
      print(y)
      x, y = y, x % y 
      print(x)
      print(y)
   print("GCD:")
   return x 

print(gcd(60,48))
print(gcd(4278, 860))
print(gcd(406,555))
print(gcd(244, 354))
