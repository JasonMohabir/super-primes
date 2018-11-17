import time
from sieve import sieve
import csv

with open('time_trial_sieve_2.csv', mode='a+') as time_trial:
    time_trial_w = csv.writer(time_trial, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    time_trial_w.writerow(['Function Name','n','# of primes','Time'])
    n = 0

    while (n != 1000000):
        start = time.time()

        retList = sieve(n)

        end = time.time()
        time_elapse = end - start
        numberOfPrimes = len(retList)

        time_trial_w.writerow(['Sieve',str(n),str(numberOfPrimes),str(time_elapse)])
        n += 10000
