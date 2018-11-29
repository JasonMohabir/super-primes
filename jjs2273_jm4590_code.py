# Jihanne Jozefe Shepherd (jjs2273)
# Jason Mohabir (jm4590)

# Import all of these modules!
import math
import numpy as np
from random import randint
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import pandas as pd

def gcd(x,y):
   while(y):
      x, y = y, x % y
   return x

def sieve(n):

    if n < 2:
        return []

    sieve = [True] * (n)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, n):
        if (i * i) > n:
            continue
        for j in range(i * i,n,i):
            sieve[j] = False
    
    return(np.array(list(range(0,n)))[sieve])

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

def prime_sieve(n):
    if sieve(n)[len(sieve(n))-1] == n:
        return True
    else:
        return False

def prime_fermat(n):
    if n == 1:
        return("Not prime")
    if n == 2 or n == 3:
        return("Prime")
    else:
        for k in range (0, 2):
            a = randint(2, n-2)
            if pow(a, n-1) % n != 1:
                return("Composite")
    return("Probably prime")

def factor_trial(n):
    retList = []

    if n < 2:
       return retList.append(n)

    while n % 2 == 0:
        retList.append(2)
        n /= 2

    factor = 3 # 2 is the only even prime                                                                                                   

    while factor * factor <= n:
        if n % factor == 0:
            retList.append(factor)
            n /= factor
        else:
            factor += 2
    if n != 1:
        retList.append(n)

def factor_pollard(n):
    retList = []

    if n < 2:
        return retList.append(n)

    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x); y = f(f(y))
        d = gcd(abs(x-y), n)
    if d != n:
        retList.extend(factor_trial(d))
        retList.extend(factor_trial(n/d))
    return retList

def visual_klauber():
   n = 500
   ncols = 2*n+1
   nmax = n**2

   # Prime numbers up to and including n**2.
   primes = np.array([n for n in range(2,n**2+1) if all(
            (n % m) != 0 for m in range(2,int(np.sqrt(n))+1))])
   a = np.zeros(nmax)
   a[primes-1]=1

   arr = np.zeros((n, ncols))
   for i in range(n):
      arr[i,(n-i):(n+i+1)] = a[i**2:i**2+2*i+1]

   fig, ax = plt.subplots()
   ax.matshow(arr, cmap=cm.binary)
   ax.axis('off')
   # Ensure the Axes are centred in the figure
   ax.set_position([0.1,0.1,0.8,0.8])
   plt.show()


def make_spiral(arr):
    nrows, ncols= arr.shape
    idx = np.arange(nrows*ncols).reshape(nrows,ncols)[::-1]
    spiral_idx = []
    while idx.size:
        spiral_idx.append(idx[0])
        # Remove the first row (the one we've just appended to spiral).
        idx = idx[1:]
        # Rotate the rest of the array anticlockwise
        idx = idx.T[::-1]
    # Make a flat array of indices spiralling into the array.
    spiral_idx = np.hstack(spiral_idx)
    # Index into a flattened version of our target array with spiral indices.
    spiral = np.empty_like(arr)
    spiral.flat[spiral_idx] = arr.flat[::-1]
    return spiral

def visual_ulam():
   # edge size of the square array.
   w = 251
   # Prime numbers up to and including w**2.
   primes = np.array([n for n in range(2,w**2+1) if all(
            (n % m) != 0 for m in range(2,int(np.sqrt(n))+1))])
   # Create an array of boolean values: 1 for prime, 0 for composite
   arr = np.zeros(w**2, dtype='u1')
   arr[primes-1] = 1
   # Spiral the values clockwise out from the centre
   arr = make_spiral(arr.reshape((w,w)))

   plt.matshow(arr, cmap=cm.binary)
   plt.axis('off')
   plt.show()


def visual_euclid():
   rows_list = []
   for i in range(0,500):
      dict = {}
      for j in range(0,500):
         d1 = {j: gcd(i,j)}
         dict.update(d1)
      rows_list.append(dict)
   df = pd.DataFrame(rows_list)
   sns.heatmap(df)
   plt.show()


while (1):
    print("""
  ____ ___ ____   ____ ____  _____ _____ _____   __  __    _  _____ _   _ 
 |  _ \_ _/ ___| / ___|  _ \| ____|_   _| ____| |  \/  |  / \|_   _| | | |
 | | | | |\___ \| |   | |_) |  _|   | | |  _|   | |\/| | / _ \ | | | |_| |
 | |_| | | ___) | |___|  _ <| |___  | | | |___  | |  | |/ ___ \| | |  _  |
 |____/___|____/ \____|_| \_\_____| |_| |_____| |_|  |_/_/   \_\_| |_| |_|
                                                                          
""")

    print("Hello! This is the Amazing Prime Numbers Project!\n")
    print("This is for COMS 3203 Discrete Mathematics Fall 2018")
    print("Sorry about the issues with the GUI as a headsup!")
    print("You can press CTRL+C to exit this program.")
    print("The code solutions to the 6 questions can be accessed here.")
    print("Which solution? <Enter number>:")
    print("\t 1 - Euclid's Algorithm \n" +
          "\t 2 - How high can you go in generating prime numbers? \n" +
          "\t 3 - Primality test \n" +
          "\t 4 - Prime factorization \n" +
          "\t 5 - Prime distribution \n" +
          "\t 6 - Prime visualization \n")

    question = input("Solution: ") 

    if (question == "1"):
        print("Euclid's Algorithm")
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print(gcd(x,y))
        print("Done with Euclid's Algorithm")

    if (question == "2"):
        print("How high can you go in generating prime numbers?")
        n = int(input("Generate primes up to: "))
        print(sieve(n))
        print("Done with Sieve of Eratosthenes")

    if (question == "3"):
        print("Primality test \n")
        print("Which primality test? <Enter number>:")
        print("\t 1 - Trial Divsion \n" +
              "\t 2 - Sieve of Eratosthenes \n" +
              "\t 3 - Fermat's Little Theorem \n")
        
        primality_test = input("Primality: ")
        if (primality_test == "1"):
            print("Trial Division Primality Test")
            n = int(input("Enter number: "))
            print(prime_trial(n))
        if (primality_test == "2"):
            print("Sieve of Eratosthenes Primality Test")
            n = int(input("Enter number: "))
            print(prime_sieve(n))
        if (primality_test == "3"):
            print("Fermat's Little Theorem Primality Test")
            n = int(input("Enter number: "))
            print(prime_fermat(n))
    
    if (question == "4"):
        print("Prime factorization \n")
        print("Which factorization method? <Enter number>:")
        print("\t 1 - Trial Division \n" +
              "\t 2 - Pollard's Rho \n")
        
        prime_factorization = input("Prime factorization:")
        if (prime_factorization == "1"):
            print("Trial Division Prime Factorization")
            n = int(input("Enter number: "))
            print(factor_trial(n))
        if (prime_factorization == "2"):
            print("Trial Division Pollard's Rho")
            n = int(input("Enter number: "))
            print(factor_pollard(n))

    if (question == "5"):
        print("Prime distribution \n")
        print("To save time, this is static data generated from n = 50000000 \n")
        with open("q5_prime_distribution.txt", 'r') as fin:
           print(fin.read())

    if (question == "6"):
       print("Prime visualization \n")
       print("Which visualization? \n" +
             "\t **Note these visualizations take time to generate**")
       print("\t 1 - Klauber's Triangle \n" +
             "\t 2 - Ulam's Spiral \n" +
             "\t 3 - Euclid's Algorithm Steps \n" +
             "\t 4 - Prime Factorization Vectors with UMAP \n")
       
       visualization = input("Visualization: ")
       if (visualization == "1"):
          print("Klauber's Triangle Visualization")
          visual_klauber()
       if (visualization == "2"):
          print("Ulam's Spiral Visualization")
          visual_ulam()
       if (visualization == "3"):
          print("Euclid's Algorithm Steps Visualization")
          visual_euclid()
       if (visualization == "4"):
          print("Prime Factorization Vectors with UMAP Visualization")
          #visual_umap()
          print("This visualization is very intensive. A copy can be found in the report. Sorry for the inconvinience.")

    else:
       print("Try again!")
       

