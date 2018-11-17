
def prime_factor_div_0(n):
    retList = []
    factor = 2

    while n > 1:
        if n % factor == 0:
            retList.append(factor)
            n /= factor
        else:
            factor += 1
    return retList

def prime_factor_div_1(n):
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
