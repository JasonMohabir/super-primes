import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import math
from scipy import stats

warnings.filterwarnings('ignore')

df = pd.read_csv('sieve_time_1.csv')
sns.regplot(df['n'],df['Time'], color ="g")

def sieve_runtime(n):
    if (n <= 1):
        return 0
    print(n)
    val = math.log(n)
    print(val)
    return(n * math.log(val))

df['algo'] = df['n'].apply(sieve_runtime)
ax2 = plt.twinx()
sns.regplot(df['n'],df['algo'], color = "b", ax=ax2)

plt.show()
