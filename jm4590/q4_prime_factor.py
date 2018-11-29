# Jason Mohabir


# Run-time efficieny: O(n^2)

def trial_div_pf_v0(n):
    retList = []
    factor = 2

    while n > 1:
        if n % factor == 0:
            retList.append(factor)
            n /= factor
        else:
            factor += 1
    return retList

def trial_div_pf_v1(n):
    retList = []
    
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

    return retList

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def pollard_rho_pf(n):
    retList = []
    if n < 2:
        return retList
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x); y = f(f(y))
        d = gcd(abs(x-y), n)
    if d != n:
        retList.extend(trial_div_pf_v1(d))
        retList.extend(trial_div_pf_v1(n/d))
    return retList

def pollard_pf(n):
    retList = []
    if n < 2:
        return retList

    if(n%2 == 0):
        retList.append(2)
        n /= 2

    x=random.randrange(2,1000000)
    c=random.randrange(2,1000000)
    y=x
    d=1
    while(d==1):
        x=(x*x+c)%n
        y=(y*y+c)%n
        y=(y*y+c)%n
        d=gcd(x-y,n)
        if(d==n):
            break;
    return d;
