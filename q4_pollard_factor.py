from random import randint

# Implement more efficient gcd algorithm with Pollard's algorithm
# Implement Pollard's, Brent's, Pollard's (p+1)
def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

def pollards_rho(n):
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x); y = f(f(y))
        d = gcd(abs(x-y), n)
    if d != n: return d

