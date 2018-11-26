import time
from sieve import sieve_v2
import csv

with open('sieve_time_1.csv', mode='a+') as time_trial:
    time_trial_w = csv.writer(time_trial, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    time_trial_w.writerow(['Function Name','n','# of primes','Time'])

    n = 0
    while (n != 100):
        start = time.time()

        retList = sieve_v2(n)

        end = time.time()
        time_elapse = end - start
        numberOfPrimes = len(retList)

        time_trial_w.writerow(['Sieve',str(n),str(numberOfPrimes),str(time_elapse)])
        n += 1

    while (n != 1000):
        start = time.time()

        retList = sieve_v2(n)

        end = time.time()
        time_elapse = end - start
        numberOfPrimes = len(retList)

        time_trial_w.writerow(['Sieve',str(n),str(numberOfPrimes),str(time_elapse)])
        n += 100

    while (n != 10000):
        start = time.time()

        retList = sieve_v2(n)

        end = time.time()
        time_elapse = end - start
        numberOfPrimes = len(retList)

        time_trial_w.writerow(['Sieve',str(n),str(numberOfPrimes),str(time_elapse)])
        n += 1000

    while (n != 1000000):
        start = time.time()

        retList = sieve_v2(n)

        end = time.time()
        time_elapse = end - start
        numberOfPrimes = len(retList)

        time_trial_w.writerow(['Sieve',str(n),str(numberOfPrimes),str(time_elapse)])
        n += 100000

    while (n != 100000000):
        start = time.time()

        retList = sieve_v2(n)

        end = time.time()
        time_elapse = end - start
        numberOfPrimes = len(retList)

        time_trial_w.writerow(['Sieve',str(n),str(numberOfPrimes),str(time_elapse)])
        n += 10000000


