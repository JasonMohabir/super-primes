import time
# Import the relevant functions
import csv

csv_name = "trial.csv"
with open(csv_name, mode='a+') as time_trial:
    time_trial_w = csv.writer(time_trial, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #time_trial_w.writerow(['n'])

    n = 10000000
    while (n != 100000000):
        start = time.time()
        retList = trial_div_pf_v1(n)
        end = time.time()
        time_elapse_td = end - start

        start = time.time()
        retList = pollard_rho_pf(n)
        end = time.time()
        time_elapse_pr = end - start

        time_trial_w.writerow([str(n),str(time_elapse_td),str(time_elapse_pr)])
        n += 1
