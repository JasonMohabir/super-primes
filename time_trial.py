import time
from sieve import sieve_v2
import csv

with open('data/time_trial_sieve_v2_4.csv', mode='a+') as time_trial:
    time_trial_w = csv.writer(time_trial, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    time_trial_w.writerow(['Function Name','n','# of primes','Time'])

    n = 1000000
    while (n != 2000000):
        start = time.time()

        retList = sieve_v2(n)

        end = time.time()
        time_elapse = end - start
        numberOfPrimes = len(retList)

        time_trial_w.writerow(['Sieve',str(n),str(numberOfPrimes),str(time_elapse)])
        n += 10000
